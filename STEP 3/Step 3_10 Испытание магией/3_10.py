"""
Испытание магией
Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/1dSxnEFfDu8

Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и решило
дать вам испытание для подтверждения уровня полученных навыков. Вам выпала великая
честь создать полноценную программу игры в "Крестики-нолики". И вот перед вами
текст с заданием самого испытания.

Техническое задание
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления
игровым процессом. Объекты этого класса будут создаваться командой:

game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке:
0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0)
и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие
за диапазон [0; 2]), то следует генерировать исключение командой:

raise IndexError('некорректно указанные индексы')
Чтобы в программе не оперировать величинами: 0 - свободная клетка;
1 - крестики и 2 - нолики, в классе TicTacToe должны быть три публичных
атрибута (атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)
В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клеткии ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки)
и False - в противном случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в
программе не писать):

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть в "Крестики-нолики" между человеком и компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.

P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.
"""
import random


class Cell:
    def __init__(self, value=0):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    def __str__(self):
        return f'{self.__value}'

    def __bool__(self):
        return True if self.__value == 0 else False


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.__pole = tuple(tuple(Cell(0) for _ in range(3)) for _ in range(3))
        self.__coords = [(i, j) for i in range(3) for j in range(3)]

    def __getitem__(self, item):
        row, col = item
        if isinstance(col, slice):  # строка
            return tuple(it.value for it in self.__pole[item[0]][col])
        elif isinstance(row, slice):  # столбец
            return tuple(self.__pole[i][col].value for i in range(3))
        return self.__pole[row][col].value

    def __setitem__(self, key, value):
        row, col = key
        self.__pole[row][col].value = value

    def __repr__(self):
        return self.__win(self.HUMAN_X), self.__win(self.COMPUTER_O)

    def __bool__(self):
        """возвращает True, если игра не окончена
        (никто не победил и есть свободные клетки)
        и False - в противном случае"""
        hum = self.is_human_win
        comp = self.is_computer_win
        draw = not len(self.__coords)
        res = any([hum, comp, draw])
        return not any([hum, comp, draw])

    def init(self):
        self.__init__()

    def __chek_ind(self, coord):
        try:
            if 0 < len(coord) <= 2:
                x, y = map(int, coord)

                if 0 <= x < 3 and 0 <= y < 3:
                    return map(int,coord)
            raise IndexError('неверный индекс клетки')

        except Exception as ex:
            raise IndexError('неверный индекс клетки')

    def __win(self, player):
        win = lambda x: x == player
        win_row = any(all(win(item.value) for item in row) for row in self.__pole)
        win_col = any(all(win(self.__pole[col][0].value) for col in range(3)) for col in range(3))
        win_main_diagonal = all(win(self.__pole[i][i].value) for i in range(3))
        win_side_diagonal = all(win(self.__pole[i][2-i].value) for i in range(3))
        return any([win_row, win_col, win_main_diagonal, win_side_diagonal])

    def show(self):
        for cell in self.__pole:
            print(*cell)
        print()

    def human_go(self):
        """реализация хода игрока(запрашивает координаты свободной
        клеткии ставит туда крестик);"""
        while True:
            coord = input("Введите координаты свободной клетки (0 1): ").split()
            x, y = self.__chek_ind(coord)

            if bool(self[x, y]):
                self[x, y] = self.HUMAN_X
                self.__coords.remove((x, y))
                break
            else:
                print(f"Клетка {x} {y} уже занята. Введите другие координаты")
                continue


    def computer_go(self):
        """реализация хода компьютера (ставит случайным
        образом нолик в свободную клетку)"""
        coord = random.choice(self.__coords)

        while True:
            x, y = self.__chek_ind(coord)

            if bool(self[x, y]):
                self[x, y] = self.COMPUTER_O
                self.__coords.remove((x,y))
                break

    @property
    def is_human_win(self):
        """возвращает True, если победил человек, иначе - False"""
        return self.__win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        """возвращает True, если победил компьютер, иначе - False"""
        return self.__win(self.COMPUTER_O)

    @property
    def is_draw(self):
        """возвращает True, если ничья, иначе - False"""
        return not len(self.__coords)


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
print(game[0, 0], game[2, 2])
print(game[0, 0] == 0, game[2, 2] == 0)
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"