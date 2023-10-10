'''
Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ

Подвиг 7. Используя информацию о модуле abc из предыдущего
подвига 6, объявите базовый класс с именем StackInterface со следующими абстрактными методами:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

На основе этого класса объявите дочерний класс с именем Stack.
Объекты этого класса должны создаваться командой:

st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут:

_top - ссылка на первый объект стека (для пустого стека _top = None).

В самом классе Stack переопределить абстрактные методы базового класса:

def push_back(self, obj) - добавление объекта в конец стека;
def pop_back(self) - удаление последнего объекта из стека.

Сами объекты стека должны определяться классом StackObj и создаваться командой:

obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка). В каждом
объекте класса StackObj должны автоматически формироваться атрибуты:

_data - информация, хранящаяся в объекте (строка);
_next - ссылка на следующий объект стека (если следующий
отсутствует, то _next = None).

Пример использования классов (эти строчки в программе писать не нужно):

st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект
(если объектов не было, то del_obj = None)
P.S. В программе требуется объявить только классы. На экран
выводить ничего не нужно.
'''
from abc import ABC, abstractmethod

# здесь объявляйте классы
class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj) -> None:
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

    @abstractmethod
    def pop_back(self):
        """
        удаление последнего объекта из односвязного списка
        :return:
        """
        if len(self.__stack) > 1:
            del self.__stack[-1]
        else:
            self.top = None
            self.__stack.clear()


class Stack(StackInterface):
    def __init__(self):
        self.__stack = list()
        self._top = None

    def push_back(self, obj) -> None:
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
            self._top = obj

    def pop_back(self):
        """
        удаление последнего объекта из односвязного списка
        :return:
        """
        if len(self.__stack) > 1:
            return self.__stack.pop()
        else:
            res, self._top = self._top, None
            self.__stack.clear()
            return res


class StackObj:
    def __init__(self, data: str=""):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, obj):
        self._next = [self._next, obj][type(obj) == type(StackObj())]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: str):
        self._data = [self._data, data][type(data) == str]


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект
# (если объектов не было, то del_obj = None)

assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"