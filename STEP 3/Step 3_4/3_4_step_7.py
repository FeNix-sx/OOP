"""
Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один объект ссылается на следующий и так далее):

Давайте снова создадим такую структуру данных. Для этого объявим два класса:

Stack - для управления односвязным списком в целом;
StackObj - для представления отдельных объектов в односвязным списком.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)
где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

Объекты класса Stack создаются командой:

st = Stack()
и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

Также в классе Stack следует объявить следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop_back(self) - удаление последнего объекта из односвязного списка.

Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):

# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.
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
        self.__next = [self.__next, obj][type(obj) == type(StackObj())]

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

    @staticmethod
    def __chek(obj):
        return type(obj) == type(StackObj())

    def __add__(self, other):
        """
        сложение с объектом класса StackObj
        :param other:
        :return:
        """
        if self.__chek(other):
            self.push_back(other)
            return self
        else:
            raise TypeError("Ошибка! Должен быть экземпляр класса StackObj")

    def __iadd__(self, other) -> None:
        """
        сложение с объектом класса StackObj
        :param other:
        :return:
        """
        return self.__add__(other)

    def __mul__(self, other):
        """
        умножение каждого числа списка на указанное число
        :param other:
        :return:
        """
        if isinstance(other, list):
            for data in other:
                self.__add__(StackObj(data))

            return self
        else:
            raise TypeError("Ошибка! Должен быть список строк")

    def __imul__(self, other):
        """
        умножение каждого числа списка на указанное число
        :param other:
        :return:
        """
        return self.__mul__(other)

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


obj = StackObj("data")
st = Stack()
print(st)
# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
print(st)
st += obj
print(st)

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', 'data_N']
st *= ['data_1', 'data_2', 'data_N']