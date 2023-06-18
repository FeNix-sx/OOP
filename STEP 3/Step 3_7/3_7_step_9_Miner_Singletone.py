"""
Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)
где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла. Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты x1, y1, x2, y2 существуют и False - в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')
Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. Два объекта должны быть созданы командой

Ellipse()
и еще два - командой:

Ellipse(x1, y1, x2, y2)
Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2. (Помните, что для этого был определен магический метод __bool__()).

P.S. На экран ничего выводить не нужно.
"""
import random

class Cell:
    """
    представление клетки игрового поля
    """

    def __init__(self):
        """"""
        # булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def number(self):
        """число мин вокруг клетки (целое число от 0 до 8)"""
        return self.__number

    @number.setter
    def number(self, val):
        """число мин вокруг клетки (целое число от 0 до 8)"""
        if isinstance(val, int) and 0 <= val <= 8:
            self.__number = val
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, val):
        if isinstance(val, bool):
            self.__is_mine = val
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        """флаг того, открыта клетка или закрыта: True - открыта; False - закрыта."""
        return self.__is_open

    @is_open.setter
    def is_open(self, val):
        """флаг того, открыта клетка или закрыта: True - открыта; False - закрыта."""
        if isinstance(val, bool):
            self.__is_open = val
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return self.__is_open == False

class GamePole:
    __instance = None
    """
    управление игровым полем, размером N x M клеток
    """
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, N, M, total_mines):
        """
        инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
        разумеется каждая мина должна находиться в отдельной клетке)
        :param N: размер поля
        :param M: общее число мин на поле
        """
        self.size_row = N
        self.size_colunm = M
        self.count_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.size_colunm)) for _ in range(self.size_row))
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        """
        инициализация начального состояния игрового поля (расставляет мины и делает все клетки закрытыми)
        :return: None
        """
        # список всех ячеек без ним, и плюс список мин
        all_cell = [0 for _ in range(self.size_row * self.size_colunm - self.count_mines)] + [1 for _ in range(self.count_mines)]
        random.shuffle(all_cell)
        # поле аналогичное минному с 0 и 1 (0 мины нет, 1 мина есть)
        total_mines = [all_cell[row*self.size_colunm:(row+1)*self.size_colunm] for row in range(self.size_row)]

        # расстановка мин
        for row in range(self.size_row):
            for col in range(self.size_colunm):
                # если мина есть (1) то значение True, если нет, то False
                self.__pole_cells[row][col].is_mine = [False, True][total_mines[row][col]]

        for row in range(self.size_row):
            for col in range(self.size_colunm):
                # количество мин вокруг
                sum_mine = self.chec_i(row - 1, col - 1) + self.chec_i(row - 1, col) + self.chec_i(row - 1, col + 1) + \
                           self.chec_i(row + 1, col - 1) + self.chec_i(row + 1, col) + self.chec_i(row + 1, col + 1) + \
                           self.chec_i(row, col - 1) + self.chec_i(row, col + 1)
                self.__pole_cells[row][col].number = sum_mine
                # закрыть ячейку
                self.__pole_cells[row][col].is_open = False

    def open_cell(self, i, j):
        """открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля;
        метод меняет значение атрибута __is_open"""
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        """отображает игровое поле в консоли (как именно сделать - на ваше усмотрение,
        этот метод - домашнее задание)."""
        for row in self.__pole_cells:
            [print("*" if cell.is_mine else cell.number, end=" ") for cell in row]
            print()

    def chec_i(self, row: int, col: int):
        """
        проверка индексов поля
        :param row: строка
        :param col: столбец
        :return: int
        """
        if 0 <= row < self.size_row:
            if 0 <= col < self.size_colunm:
                res = self.__pole_cells[row][col].is_mine
                return int(res)
        return 0


pole = GamePole(10, 20, 20)  # создается поле размерами 10x20 с общим числом мин 10

pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()

##########################
p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"



