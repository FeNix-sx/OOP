"""
Подвиг 9 (релакс). Объявите класс с именем Dimensions, объекты которого создаются командой:

d = Dimensions(a, b, c)
где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина и глубина.

Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми значениями). Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.

С помощью функции input() прочитайте из входного потока строку, записанную в формате:

"a1 b1 c1; a2 b2 c2; ... ;aN bN cN"

Например:

"1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна генерироваться ошибка командой:

raise ValueError("габаритные размеры должны быть положительными числами")
Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте этот список по возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за другом.

P.S. На экран ничего выводить не нужно.
"""
class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, name, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, name, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))



s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"
# s_inp = input()
lst_dims = []

for item in s_inp.split(";"):
    lst_dims.append(Dimensions(*list(map(float, item.split()))))

lst_dims.sort(key=hash)