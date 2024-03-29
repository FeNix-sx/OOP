"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kmmvxZWxaAY

Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:

Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)
где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')
При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class IntegerValue:
    """ ДИСКРИПТОР ДАННЫХ"""
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, int) and value >= 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError('возможны только целочисленные значения')


class Cell:
    def __init__(self, data=0):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

class TableValues:
    _rows = IntegerValue()
    _cols = IntegerValue()

    def __init__(self, rows, cols, type_data=int):
        self._rows = rows
        self._cols = cols
        self._type = type_data
        self._cells = tuple(tuple(Cell() for _ in range(self._cols)) for _ in range(self._rows))

    def __check_indx(self, indx):
        r, c = indx
        if not(type(r) == int and type(c) == int and 0 <= r <self._rows and 0 <= c <self._cols):
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        self.__check_indx(key)
        r, c = key

        if not self._type == type(value):
            raise TypeError('неверный тип присваиваемых данных')

        self._cells[r][c].value = value

    def __getitem__(self, item):
        self.__check_indx(item)
        r, c = item
        return self._cells[r][c].value

    def __iter__(self):
        for row in self._cells:
            yield (r.data for r in row)


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"