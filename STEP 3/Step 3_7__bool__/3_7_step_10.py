"""
Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')
P.S. В программе на экран выводить ничего не нужно, только объявить класс.
"""
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __len__(self):
        return len(self.__coords)

    def __add__(self, other):
        """суммирование соответствующих координат векторов, новые объекты класса Vector"""
        if isinstance(other, Vector):
            if len(self) == len(other):
                coord = [self.__coords[i] + other.__coords[i] for i in range(len(self))]
                return Vector(*coord)
            raise ArithmeticError('размерности векторов не совпадают')
        raise TypeError('Не верный формат данных')

    def __sub__(self, other):
        """вычитание соответствующих координат векторов, новые объекты класса Vector"""
        if isinstance(other, Vector):
            if len(self) == len(other):
                coord = [self.__coords[i] - other.__coords[i] for i in range(len(self))]
                return Vector(*coord)
            raise ArithmeticError('размерности векторов не совпадают')
        raise TypeError('Не верный формат данных')

    def __mul__(self, other):
        """умножение соответствующих координат векторов, новые объекты класса Vector"""
        if isinstance(other, Vector):
            if len(self) == len(other):
                coord = [self.__coords[i] * other.__coords[i] for i in range(len(self))]
                return Vector(*coord)
            raise ArithmeticError('размерности векторов не совпадают')
        raise TypeError('Не верный формат данных')

    def __iadd__(self, num):
        """суммирование координат с числом, новые объекты класса Vector"""
        if isinstance(num, (int, float)):
            self.__coords = [self.__coords[i] + num for i in range(len(self))]
            return self
        elif isinstance(num, Vector):
            self.__coords = (self + num).__coords
            return self
        raise TypeError('Не верный формат данных')

    def __isub__(self, num):
        """вычитание из всех координат вектора числа 10, новые объекты класса Vector"""
        if isinstance(num, (int, float)):
            self.__coords = [self.__coords[i] - num for i in range(len(self))]
            return self
        elif isinstance(num, Vector):
            self.__coords = (self - num).__coords
            return self
        raise TypeError('Не верный формат данных')

    def __eq__(self, other):
        """True, если соответствующие координаты векторов равны"""
        if isinstance(other, Vector):
            if len(self) == len(other):
                return all([self.__coords[i] == other.__coords[i] for i in range(len(self))])

            raise ArithmeticError('размерности векторов не совпадают')
        raise TypeError('Не верный формат данных')

    @property
    def coords(self):
        return self.__coords

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True