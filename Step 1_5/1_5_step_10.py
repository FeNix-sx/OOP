"""
Большой подвиг 10. Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь
    around_mines - число мин вокруг данной клетки поля;
    mine - булева величина (True/False), означающая наличие мины в текущей клетке.
При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

    around_mines - число мин вокруг клетки (начальное значение 0);
    mine - наличие мины в текущей клетке (True/False);
    fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).

С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь
    N - размер поля;
    M - общее число мин на поле.
При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном
списке N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка
не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init()
для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.

P.S. На экран в программе ничего выводить не нужно.
"""
import random


class Cell:
    """
    представление клетки игрового поля
    """
    def __init__(self, around_mines: int=0, mine: bool=False):
        """
        :param around_mines: число мин вокруг данной клетки поля;
        :param mine: булева величина (True/False), означающая наличие мины в текущей клетке
        """
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = random.choice([True, False])

class GamePole:
    """
    управление игровым полем, размером N x N клеток
    """

    def __init__(self, N, M):
        """
        инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
        разумеется каждая мина должна находиться в отдельной клетке)
        :param N: размер поля
        :param M: общее число мин на поле
        """
        self.size_field = N
        self.count_mines = M
        self.init()

    def init(self):
        """
        инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
        разумеется каждая мина должна находиться в отдельной клетке)
        :return: None
        """
        all_mines = [1 for _ in range(self.count_mines)]
        all_cell = [0 for _ in range(self.size_field ** 2 - self.count_mines)] + all_mines
        random.shuffle(all_cell)

        field = list()
        for _ in range(self.size_field):
            field.append(all_cell[:self.size_field])
            all_cell = all_cell[self.size_field:]

        self.pole = [[Cell(0, [0, "*"][i]) for i in item] for item in field]

        for row in range(self.size_field):
            for col in range(self.size_field):
                sum_mine = self.chec_i(row-1, col-1) + self.chec_i(row-1, col) + self.chec_i(row-1, col+1) + \
                         self.chec_i(row+1, col-1) + self.chec_i(row+1, col) + self.chec_i(row+1, col+1) + \
                         self.chec_i(row, col-1) + self.chec_i(row, col+1)
                self.pole[row][col].around_mines = sum_mine.count("*")

    def chec_i(self, row: int, col: int):
        """
        проверка индексов поля
        :param row: строка
        :param col: столбец
        :return: str
        """
        if 0 <= row < self.size_field:
            if 0 <= col < self.size_field:
                return str(self.pole[row][col].mine)
        return ""

    def show(self):
        for rows in self.pole:
            func_out = lambda x: [x.around_mines, x.mine][x.mine=="*"] if x.fl_open else "#"
            print(*map(func_out, rows))


pole_game = GamePole(20, 200)
pole_game.show()
