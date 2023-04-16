"""
Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")
Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)
Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

P.S. На экран в программе выводить ничего не нужно.
"""
class FloatValue:
    @staticmethod
    def __check_num(number):
        if type(number) == float:
            return number
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, self.__check_num(value))


class IntegerValue:
    @staticmethod
    def __check_num(number):
        if type(number) == int:
            return number
        else:
            raise TypeError("Присваивать можно только целые числа.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, self.__check_num(value))


class Cell:
    value = FloatValue()

    def __init__(self, value: float = 0.0):
        self.value = value


class TableSheet:
    N = IntegerValue()
    M = IntegerValue()

    def __init__(self, N: int, M: int):
        self.N = N
        self.M = M
        self.__cells = [[Cell() for _ in range(self.M)] for _ in range(self.N)]

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, lst_value: list):
        if lst_value and len(lst_value) == self.N * self.M:
            self.__cells = [[Cell(float(lst_value.pop(0))) for _ in range(self.M)] for _ in range(self.N)]


# ts = TableSheet(5, 3)
# tb = TableSheet(5, 3)
table  = TableSheet(5, 3)
print(table.cells)
print(table.cells[1][1].value)

table.cells = list(range(1,16))
print([[cell.value for cell in row] for row in table.cells])
