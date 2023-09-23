"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Q_zIap6F1Lw

Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих
координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной.
Иначе, v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""

class Vector:
    def __init__(self, *args):
        self.coord = list(args)

    def __check_size(self, other):
        return len(self.coord) == len(other.coord)

    def __add__(self, other):
        if not self.__check_size(other):
            raise TypeError('размерности векторов не совпадают')
        new_coord = tuple(x1 + x2 for x1, x2 in zip(self.coord, other.coord))

        if not self.check_int(new_coord, int):
            return Vector(*new_coord)
        return VectorInt(*new_coord)

    def __sub__(self, other):
        if not self.__check_size(other):
            raise TypeError('размерности векторов не совпадают')
        new_coord = tuple(x1 - x2 for x1, x2 in zip(self.coord, other.coord))

        if not self.check_int(new_coord, int):
            return Vector(*new_coord)
        return VectorInt(*new_coord)

    def get_coords(self):
        return tuple(self.coord)

    def check_int(self, coord, type):
        return all([isinstance(item, type) for item in coord])


class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        if not self.check_int(self.coord, int):
            raise ValueError('координаты должны быть целыми числами')



v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
print((v1+v2).get_coords())
assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"