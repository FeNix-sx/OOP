"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/oKBKLVb21nY

Подвиг 10. Вам необходимо описывать в программе очень большие и разреженные таблицы данных (с большим числом пропусков). Для этого предлагается объявить класс SparseTable, объекты которого создаются командой:

st = SparseTable()
В каждом объекте этого класса должны создаваться локальные публичные атрибуты:

rows - общее число строк таблицы (начальное значение 0);
cols - общее число столбцов таблицы (начальное значение 0).

В самом классе SparseTable должны быть объявлены методы:

add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа);
remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами (row, col).

При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, cols объекта класса SparseTable. Если происходит попытка удалить несуществующую ячейку, то должно генерироваться исключение:

raise IndexError('ячейка с указанными индексами не существует')
Ячейки таблицы представляют собой объекты класса Cell, которые создаются командой:

data = Cell(value)
где value - данные ячейки (любой тип).

Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell.

Также с объектами класса SparseTable должны выполняться команды:

res = st[i, j] # получение данных из таблицы по индексам (i, j)
st[i, j] = value # запись новых данных по индексам (i, j)
Чтение данных возможно только для существующих ячеек. Если ячейки с указанными индексами нет, то генерировать исключение командой:

raise ValueError('данные по указанным индексам отсутствуют')
При записи новых значений их следует менять в существующей ячейке или добавлять новую, если ячейка с индексами (i, j) отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols).

Пример использования классов (эти строчки в программе не писать):

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class IntegerValue:
    """ ДИСКРИПТОР ДАННЫХ"""
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not(isinstance(value, int) and value >= 0):
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class Cell:
    def __init__(self, start_value=None):
        self.value = start_value


class SparseTable:
    rows = IntegerValue()
    cols = IntegerValue()

    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.cells = dict()

    def __cells(self, rows, cols):
        if (rows, cols) not in self.cells.keys():
            self.cells[(rows, cols)] = Cell()
            # self.rows += 1
            # self.cols += 1
            self.rows = max(self.cells.keys(), key=lambda x: x[0])[0]+1
            self.cols = max(self.cells.keys(), key=lambda x: x[1])[1]+1

    def __ckeck_key(self, row, col):
        if not((row, col) in self.cells.keys()):
            raise IndexError('ячейка с указанными индексами не существует')

    def add_data(self, row, col, data):
        """добавление данных data (объект класса Cell)
        в таблицу по индексам row, col (целые неотрицательные числа);"""
        self.__cells(row, col)
        self.cells[(row, col)].value = data

    def remove_data(self, row, col):
        """удаление ячейки (объект класса Cell) с индексами (row, col)."""
        self.__ckeck_key(row, col)
        del self.cells[(row, col)]
        # self.rows -= 1
        # self.cols -= 1
        self.rows = max(self.cells.keys(), key=lambda x: x[0])[0]+1
        self.cols = max(self.cells.keys(), key=lambda x: x[1])[1]+1

    def __getitem__(self, item):
        r, c = item
        if not(item in self.cells.keys()):
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.cells[(r, c)].value

    def __setitem__(self, key, value):
        r, c = key
        self.__cells(r, c)
        self.cells[(r, c)].value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

# print(st[3,2])
st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"