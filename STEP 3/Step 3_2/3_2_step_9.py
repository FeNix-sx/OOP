"""
Подвиг 8 (развитие подвига 7). Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять
к функциям следующим образом:

@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"
Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки. Сама декорированная
функция вызывается по аналогии с предыдущим подвигом:

res = contact({"method": "POST", "url": "contact.html"})
В результате функция contact должна возвращать строку в формате:

"<метод>: <данные из функции>"

В нашем примере - это будет:

"POST: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если ключ method принимает
значение отсутствующее в списке methods декоратора Handler, например, "PUT", то декорированная функция contact
должна возвращать значение None.

Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:

def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса

В зависимости от типа запроса должен вызываться соответствующий метод (его выбор в классе можно реализовать
методом __getattribute__()). На выходе эти методы должны формировать строки в заданном формате.

P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.

Небольшая справка
Для реализации декоратора с параметрами на уровне класса в инициализаторе __init__(self, methods) прописываем
параметр для декоратора, а магический метод __call__() объявляем как полноценный декоратор на уровне функции, например:

class Handler:
    def __init__(self, methods):
        # здесь нужные строчки

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            # здесь нужные строчки
        return wrapper
"""
class Handler:
    def __init__(self, methods = ('GET',)):
        self.__methods = methods
        # здесь нужные строчки

    def __call__(self, func,*args, **kwargs):
        def wrapper(request: dict, *args, **kwargs):
            if "method" not in request.keys():
                return self.get(func, request)

            elif request.get("method", "GET") in self.__methods:
                return {
                    "GET": self.get(func, request),
                    "POST": self.post(func, request)
                }[request["method"]]
            else:
                return None
            # здесь нужные строчки
        return wrapper

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request, *args, **kwargs)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request, *args, **kwargs)}"



@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"

res = contact(dict())
print(res)