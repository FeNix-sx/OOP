"""
Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:

MoneyR - для рублевых кошельков
MoneyD - для долларовых кошельков
MoneyE - для евро-кошельков

Объекты этих классов могут создаваться командами:

rub = MoneyR()   # с нулевым балансом
dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро
В каждом объекте этих классов должны формироваться локальные атрибуты:

__cb - ссылка на класс CentralBank (центральный банк, изначально None);
__volume - объем денежных средств в кошельке (если не указано, то 0).

Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property) для работы с локальными атрибутами:

cb - для изменения и считывания данных из переменной __cb;
volume - для изменения и считывания данных из переменной __volume.

Объекты классов должны поддерживать следующие операторы сравнения:

rub < dl
dl >= euro
rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
euro > rub
При реализации операторов сравнения считываются соответствующие значения __volume из сравниваемых объектов и приводятся к рублевому эквиваленту в соответствии с курсом валют центрального банка.

Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки, необходимо в программе объявить еще один класс CentralBank. Объекты класса CentralBank создаваться не должны (запретить), при выполнении команды:

cb = CentralBank()

должно просто возвращаться значение None. А в самом классе должен присутствовать атрибут:

rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
Здесь числа (в значениях словаря) - курс валюты по отношению к доллару.

Также в CentralBank должен быть метод уровня класса:

register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и MoneyE.

При регистрации значение __cb объекта money должно ссылаться на класс CentralBank. Через эту переменную объект имеет возможность обращаться к атрибуту rates класса CentralBank и брать нужные котировки.

Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:

raise ValueError("Неизвестен курс валют.")
Пример использования классов (эти строчки в программе писать не нужно):

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
P.S. В программе на экран ничего выводить не нужно, только объявить классы.
"""
class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyR:
    def __init__(self, volume: int=0):
        self.__cb = None
        self.__volume = [0, volume][self.__check_value(volume)]

    @staticmethod
    def __check_value(val):
        if val:
            return True
        return False

    @staticmethod
    def __check_cb(cb):
        if not cb:
            raise ValueError("Неизвестен курс валют.")

    def calculate(self):
        return self.volume / self.cb.rates['rub']

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb: CentralBank=None):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vol: float=0):
        self.__volume = vol

    def __eq__(self, other):
        """равно"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return abs(a - b) <= 0.1

    def __lt__(self, other):
        """меньше"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return a < b

    def __le__(self, other):
        """меньше или равно"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return a - b >= 0.1


class MoneyD:
    def __init__(self, volume: int=0):
        self.__cb = None
        self.__volume = [0, volume][self.__check_value(volume)]

    def calculate(self):
        return self.volume / self.cb.rates['dollar']

    @staticmethod
    def __check_value(val):
        if val:
            return True
        return False

    @staticmethod
    def __check_cb(cb):
        if not cb:
            raise ValueError("Неизвестен курс валют.")

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb: CentralBank=None):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vol: float=0):
        self.__volume = vol

    def __eq__(self, other):
        """равно"""
        a = self.calculate()
        b = other.calculate()
        return abs(a - b) <= 0.1

    def __lt__(self, other):
        """меньше"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return a < b

    def __le__(self, other):
        """меньше или равно"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return b - a >= 0.1

    def __ge__(self, other):
        """больше или равно"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return a - b >= 0.1

class MoneyE:
    def __init__(self, volume: int=0):
        self.__cb = None
        self.__volume = [0, volume][self.__check_value(volume)]

    def calculate(self):
        return self.volume / self.cb.rates['euro']

    @staticmethod
    def __check_value(val):
        if val:
            return True
        return False

    @staticmethod
    def __check_cb(cb):
        if not cb:
            raise ValueError("Неизвестен курс валют.")

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb: CentralBank=None):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, vol: float=0):
        self.__volume = vol

    def __eq__(self, other):
        """равно"""
        a = self.calculate()
        b = other.calculate()
        return abs(a - b) <= 0.1

    def __lt__(self, other):
        """меньше"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return a < b

    def __le__(self, other):
        """меньше или равно"""
        self.__check_cb(self.cb)
        self.__check_cb(other.cb)
        a = self.calculate()
        b = other.calculate()
        return b - a >= 0.1



# rub = MoneyR()  # с нулевым балансом
# dl = MoneyD(1501.25)  # с балансом в 1501.25 долларов
# euro = MoneyE(100)  # с балансом в 100 евро
# print(rub.cb)
# CentralBank.register(rub)
# print(rub.cb)
# CentralBank.register(dl)
# CentralBank.register(euro)
# print(rub.cb)



# Тест сугубо для помощи тем кто пытается решить своими силами.
# Я тоже учусь, просто помогаю как умею
# TEST-TASK___________________________________
bank = CentralBank()
assert bank is None, "объекты CentralBank создаваться не должны"
assert hasattr(CentralBank, "rates"), "в классе нет атрибута rates"
assert type(CentralBank.rates) is dict, "rates должен быть словарём"
assert CentralBank.rates['rub'] == 72.5 and CentralBank.rates['dollar'] == 1.0 and \
           CentralBank.rates['euro'] == 1.15, "ошибка в значениях валют"
assert hasattr(CentralBank, "register") and callable(CentralBank.register), "вы не объявили метод - register"

# проверка значений по умолчанию
rub = MoneyR()  # с нулевым балансом
assert rub.__dict__['_MoneyR__cb'] == None, "изначально __cb == None"
assert rub.__dict__['_MoneyR__volume'] == 0, "если сумма не указана, то  __volume == 0"
dl = MoneyD()  # с нулевым балансом
assert dl.__dict__['_MoneyD__cb'] == None, "изначально __cb == None"
assert dl.__dict__['_MoneyD__volume'] == 0, "если сумма не указана, то  __volume == 0"
euro = MoneyE()  # с нулевым балансом
assert euro.__dict__['_MoneyE__cb'] == None, "изначально __cb == None"
assert euro.__dict__['_MoneyE__volume'] == 0, "если сумма не указана, то  __volume == 0"

# проверка записи и считывания значений
rub.cb = 111
assert rub.__dict__["_MoneyR__cb"] == 111, "некорректно работает запись в значение cb"
assert rub.cb == 111, "некорректно работает считывание значения из cb"
rub.volume = 111
assert rub.__dict__["_MoneyR__volume"] == 111, "некорректно работает запись в значение volume"
assert rub.volume == 111, "некорректно работает считывание значения из volume"

dl.cb = 111
assert dl.__dict__["_MoneyD__cb"] == 111, "некорректно работает запись в значение cb"
assert dl.cb == 111, "некорректно работает считывание значения из cb"
dl.volume = 111
assert dl.__dict__["_MoneyD__volume"] == 111, "некорректно работает запись в значение volume"
assert dl.volume == 111, "некорректно работает считывание значения из volume"

euro.cb = 111
assert euro.__dict__["_MoneyE__cb"] == 111, "некорректно работает запись в значение cb"
assert euro.cb == 111, "некорректно работает считывание значения из cb"
euro.volume = 111
assert euro.__dict__["_MoneyE__volume"] == 111, "некорректно работает запись в значение volume"
assert euro.volume == 111, "некорректно работает считывание значения из volume"
# end проверка записи и считывания значений


rub = MoneyR()  # с нулевым балансом
dl = MoneyD(1501.25)  # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро

assert isinstance(rub, MoneyR) and isinstance(dl, MoneyD) and isinstance(euro, MoneyE), \
    "необходимо создать 3 объекта rub, dl, euro"
# проверка атрибутов в классах
assert hasattr(rub, '_MoneyR__cb') and hasattr(rub, '_MoneyR__volume'), \
    "ошибка атрибуты должны быть приватными в объекте rub"
assert hasattr(dl, '_MoneyD__cb') and hasattr(dl, '_MoneyD__volume'), \
    "ошибка атрибуты должны быть приватными в объекте dl"
assert hasattr(euro, '_MoneyE__cb') and hasattr(euro, '_MoneyE__volume'), \
    "ошибка атрибуты должны быть приватными в объекте euro"

# проверяем есть ли объекты свойства в классах для обращения к приватным атрибутам __cb / __volume
assert isinstance(MoneyR.cb, property) and isinstance(MoneyR.volume, property), \
    "в классе MoneyR ошибка в наличии объектов свойств"
assert isinstance(MoneyD.cb, property) and isinstance(MoneyD.volume, property), \
    "в классе MoneyD ошибка в наличии объектов свойств"
assert isinstance(MoneyE.cb, property) and isinstance(MoneyE.volume, property), \
    "в классе MoneyE ошибка в наличии объектов свойств"

# проверка работы register
try:
    # попытка регистрации кошельков
    CentralBank.register(rub)
    CentralBank.register(dl)
    CentralBank.register(euro)
except:
    print("произошла ошибка при регистрации кошельков")
else:
    assert rub.cb == CentralBank and euro.cb == CentralBank and dl.cb == CentralBank, \
        "\nпри регистрации кошелька в банке, произошла ошибка в каком-то из кошельков\n" \
        "стоит проверить атрибут __cb в ваших кошельках или сам метод register\n" \
        "При регистрации значение __cb объекта money должно ссылаться на класс CentralBank"

# проверка объявления методов в MoneyR
assert hasattr(MoneyR, "__gt__"), "не объявлен метод __gt__ (>) в классе MoneyR"
assert hasattr(MoneyR, "__lt__"), "не объявлен метод __lt__ (<) в классе MoneyR"
assert hasattr(MoneyR, "__eq__"), "не объявлен метод __eq__ (==) в классе MoneyR"
assert hasattr(MoneyR, "__ne__"), "не объявлен метод __ne__ (!=) в классе MoneyR"
assert hasattr(MoneyR, "__ge__"), "не объявлен метод __ge__ (>=) в классе MoneyR"
assert hasattr(MoneyR, "__le__"), "не объявлен метод __le__ (<=) в классе MoneyR"
# проверка объявления методов в MoneyD
assert hasattr(MoneyD, "__gt__"), "не объявлен метод __gt__ (>) в классе MoneyD"
assert hasattr(MoneyD, "__lt__"), "не объявлен метод __lt__ (<) в классе MoneyD"
assert hasattr(MoneyD, "__eq__"), "не объявлен метод __eq__ (==) в классе MoneyD"
assert hasattr(MoneyD, "__ne__"), "не объявлен метод __ne__ (!=) в классе MoneyD"
assert hasattr(MoneyD, "__ge__"), "не объявлен метод __ge__ (>=) в классе MoneyD"
assert hasattr(MoneyD, "__le__"), "не объявлен метод __le__ (<=) в классе MoneyD"
# проверка объявления методов в MoneyE
assert hasattr(MoneyE, "__gt__"), "не объявлен метод __gt__ (>) в классе MoneyE"
assert hasattr(MoneyE, "__lt__"), "не объявлен метод __lt__ (<) в классе MoneyE"
assert hasattr(MoneyE, "__eq__"), "не объявлен метод __eq__ (==) в классе MoneyE"
assert hasattr(MoneyE, "__ne__"), "не объявлен метод __ne__ (!=) в классе MoneyE"
assert hasattr(MoneyE, "__ge__"), "не объявлен метод __ge__ (>=) в классе MoneyE"
assert hasattr(MoneyE, "__le__"), "не объявлен метод __le__ (<=) в классе MoneyE"

# проверка работы методов сравнения и т.д.
assert dl > rub, "метод > работает некорректно"
assert not dl < rub, "метод < работает некорректно"
print(dl.calculate(), euro.calculate())
assert dl >= euro, "метод >= работает некорректно"
assert not dl <= euro, "метод >= работает некорректно"
assert rub != euro, "метод != работает некорректно"
assert euro > rub, "метод > работает некорректно"
assert euro < dl, "метод < работает некорректно"
assert not euro > dl, "метод > работает некорректно"
assert not dl < euro, "метод < работает некорректно"

assert not rub == euro, "метод == работает некорректно"
assert not dl == euro, "метод == работает некорректно"
assert euro == euro, "метод == работает некорректно"

# проверка вывода ошибки если кошелёк не зарегистрирован банке
rub_test = MoneyR(72.5)
try:
    rub_test == dl
except ValueError:
    assert True
else:
    assert False, "\nВы забыли учесть условие из задачи:\n" \
                  "Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:" \
                  "raise ValueError('Неизвестен курс валют.')"

rub_test = MoneyR(72.5)
CentralBank.register(rub_test)
dl_test = MoneyD(1)
CentralBank.register(dl_test)
assert rub_test == dl_test, "\nскорее всего у вас проблема в понятии условия:\n" \
                            "- Значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)\n" \
                            "Пояснение:\n" \
                            "Означает, что при сравнении значений с определенным курсом валют, который устанавливается центральным банком,\n" \
                            "допускается погрешность в размере 0.1.\n" \
                            "Это означает, что если значения отличаются друг от друга на 0.1 или менее, то они считаются одинаковыми или эквивалентными\n" \
                            "с точки зрения сравнения по текущему курсу центрального банка.\n" \
                            "Если же разница между значениями больше чем 0.1, то эти значения считаются различными."
rub_test = MoneyR(79.75)
CentralBank.register(rub_test)
assert not rub_test == dl_test, "\nскорее всего у вас проблема в понятии условия:\n" \
                                "- Значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)\n" \
                                "Пояснение:\n" \
                                "Означает, что при сравнении значений с определенным курсом валют, который устанавливается центральным банком,\n" \
                                "допускается погрешность в размере 0.1.\n" \
                                "Это означает, что если значения отличаются друг от друга на 0.1 или менее, то они считаются одинаковыми или эквивалентными\n" \
                                "с точки зрения сравнения по текущему курсу центрального банка.\n" \
                                "Если же разница между значениями больше чем 0.1, то эти значения считаются различными."

print("Вы справились !!!!!! Я просто в шоке ))))")