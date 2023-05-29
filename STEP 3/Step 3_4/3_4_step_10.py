"""
Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска), объекты которого создаются командой:

box = Box3D(width, height, depth)
где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)

В каждом объекте класса Box3D должны создаваться публичные атрибуты:

width, height, depth - ширина, высота и глубина соответственно.

С объектами класса Box3D должны выполняться следующие операторы:

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.

P.S. В программе достаточно только объявить класс Box3D. На экран ничего выводить не нужно.

"""

from typing import Union, Type
class Box3D:
    def __init__(self, width: int|float=0, height: int|float=0, depth: int|float=0) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    @staticmethod
    def __check_val(other: Union[int, float, Type['Box3D']]) -> list | int | float:
        if isinstance(other, (int, float)):
            return other
        elif isinstance(other, Box3D):
            return [other.width, other.height, other.depth]
        else:
            raise TypeError("Ошибка! Неверный тим данных")

    def __add__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        check_val = self.__check_val(other)

        if isinstance(check_val, list):
            return Box3D(
                self.width + check_val[0], self.height + check_val[1], self.depth + check_val [2]
            )
        return Box3D(
            self.width + check_val, self.height + check_val, self.depth + check_val
        )

    def __radd__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        return self.__add__(other)

    def __mul__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        check_val = self.__check_val(other)

        if isinstance(check_val, list):
            return Box3D(
                self.width * check_val[0], self.height * check_val[1], self.depth * check_val[2]
            )
        return Box3D(
            self.width * check_val, self.height * check_val, self.depth * check_val
        )

    def __rmul__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        return self.__mul__(other)

    def __sub__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        check_val = self.__check_val(other)

        if isinstance(check_val, list):
            return Box3D(
                self.width - check_val[0], self.height - check_val[1], self.depth - check_val[2]
            )
        return Box3D(
            self.width - check_val, self.height - check_val, self.depth - check_val
        )

    def __rsub__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        return self.__add__(other)

    def __floordiv__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        check_val = self.__check_val(other)

        if isinstance(check_val, list) and 0 not in check_val:
            return Box3D(
                self.width // check_val[0], self.height // check_val[1], self.depth // check_val[2]
            )
        elif check_val != 0:
            return Box3D(
                self.width // check_val, self.height // check_val, self.depth // check_val
            )
        else:
            raise ZeroDivisionError("Ошибка! Деление на 0!")

    def __mod__(self, other: Union[int, float, Type['Box3D']]) -> Type['Box3D']:
        check_val = self.__check_val(other)

        if isinstance(check_val, list) and 0 not in check_val:
            return Box3D(
                self.width % check_val[0], self.height % check_val[1], self.depth % check_val[2]
            )
        elif check_val != 0:
            return Box3D(
                self.width % check_val, self.height % check_val, self.depth % check_val
            )
        else:
            raise ZeroDivisionError("Ошибка! Деление на 0!")


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
print(box.width, box.height, box.depth )
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
print(box.width, box.height, box.depth )
box = 3 * box2    # Box3D: width=6, height=12, depth=18
print(box.width, box.height, box.depth )
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
print(box.width, box.height, box.depth )
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
print(box.width, box.height, box.depth )
box = box2 % 3    # Box3D: width=2, height=1, depth=0
print(box.width, box.height, box.depth )