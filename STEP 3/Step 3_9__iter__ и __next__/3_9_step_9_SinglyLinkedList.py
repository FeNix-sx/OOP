"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/WrZ1TMwuvis

Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ

Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно связаны между собой:



Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)
где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class StackObj:
    def __init__(self, data: str=""):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, obj):
        self.__next = [None, obj][type(obj) == type(StackObj())]

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = [self.__data, data][type(data) == str]


class Stack:
    def __init__(self):
        self.__stack = list()
        self.top = None

    def __getitem__(self, item):
        if isinstance(item, int) and abs(item) < len(self.__stack):
            return self.__stack[item].data
        raise IndexError('неверный индекс')

    def __iter__(self):
        for item in self.__stack:
            yield item

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self.__stack):
            self.__stack[key].data = value
            self.__stack[key].next = self.__stack[key+1] if key+1 < len(self.__stack) else None
            if key > 0:
                self.__stack[key-1].next = self.__stack[key]
            return
        raise IndexError('неверный индекс')

    def push_back(self, obj:StackObj) -> None:
        """
        добавление объекта класса StackObj в конец односвязного списка
        :param obj:
        :return:
        """
        if self.__stack:
            self.__stack[-1].next = obj
            self.__stack.append(obj)
        else:
            self.__stack.append(obj)
            self.top = obj

    def push_front(self, obj:StackObj) -> None:
        """
        добавление объекта класса StackObj в начало стека
        :param obj:
        :return:
        """
        if self.__stack:
            self.__stack.insert(0, obj)
            self.top = obj
        else:
            self.__stack.append(obj)
            self.top = obj

    def pop(self) -> None:
        """
        удаление последнего объекта из односвязного списка
        :return:
        """
        if len(self.__stack) > 1:
            self.__stack[-2].next = None
            return self.__stack.pop(-1)
        else:
            self.top = None
            self.__stack.clear()

    def __len__(self):
        return len(self.__stack)


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"