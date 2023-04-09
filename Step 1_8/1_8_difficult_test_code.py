class Data:
    """
    Описание пакета информации
    """
    def __init__(self, msg: str, ip: int):
        self.data = msg
        self.ip = ip

class Server:
    """
    Описание работы серверов в сети
    """
    IP = 0

    @classmethod
    def my_ip(cls):
        ip = cls.IP + 1
        cls.IP = ip
        return ip

    def __init__(self):
        self.ip = self.my_ip()
        self.buffer = list()
        self.router: Router = None

    def send_data(self, data: Data):
        """
        Отправка информационного пакета data (объекта класса Data) с указанным IP-адресом
        получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном
        свойстве buffer);
        """
        if self.router:
            self.router.buffer[data.ip] = self.router.buffer.get(data.ip, []) + [data]

    def get_data(self):
        """
        Возвращает список принятых пакетов (если ничего принято не было, то возвращается
        пустой список) и очищает входной буфер
        :return:
        """
        buffer, self.buffer = self.buffer[:], list()
        return buffer

    def get_ip(self):
        """
        Возвращает свой IP-адрес
        :return:
        """
        return self.ip

class Router:
    """
    Описание работы роутеров в сети (в данной задаче полагается один роутер)
    """

    def __init__(self):
        self.servers = dict()
        self.buffer = dict()

    def link(self, server: Server):
        """
        Присоединение сервера server (объекта класса Server) к роутеру
        (для простоты, каждый сервер соединен только с одним роутером)
        """
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server: Server):
        """
        Отсоединение сервера server (объекта класса Server) от роутера;
        """
        if server.ip in self.servers.keys():
            server.router = None
            del self.servers[server.ip]

    def send_data(self):
        """
        Отправка всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for ip, data in self.buffer.items():
            if ip in self.servers.keys():
                self.servers[ip].buffer.extend(data)

        self.buffer = dict()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_from)
print(msg_lst_to)
print(sv_from.buffer)
assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
