"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/yX9qxE8X1OA

Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами.
Объекты этого класса должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)
где rows, cols - число строк и столбцов матрицы;
fill_value - заполняемое начальное значение элементов
матрицы (должно быть число: целое или вещественное).
Если в качестве аргументов передаются не числа, то генерировать исключение:
raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
Также объекты можно создавать командой:

m2 = Matrix(list2D)
где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных).
Если список list2D не прямоугольный, или хотя бы один из его
элементов не число, то генерировать исключение командой:
raise TypeError('список должен быть прямоугольным, состоящим из чисел')
Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')
Если указываются недопустимые индексы матрицы (должны быть целыми
числами от 0 и до размеров матрицы), то генерировать исключение:

raise IndexError('недопустимые значения индексов')
Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
Во всех этих операция должна формироваться новая матрица с соответствующими значениями.
Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')
Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""


class Matrix:
    def __init__(self, rows: int, cols: int=None, fill_value=None)->None:
        if isinstance(rows, list):
            len_it = len(rows[0])
            if not all([len_it == len(item) for item in rows]):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            if not all(all([type(item) in (int, float) for item in row]) for row in rows):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.matrix = rows
            self.rows = len(rows)
            self.cols = len(rows[0])
        elif type(fill_value) in (int, float) and isinstance(rows, int) and isinstance(cols, int):
            self.rows = rows
            self.cols = cols
            self.matrix = [[fill_value] * self.cols for _ in range(self.rows)]
        else:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')


    def __getitem__(self, indices):
        row, col = indices
        if not isinstance(row, int) or not isinstance(col, int):
            raise IndexError('недопустимые значения индексов')
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError('недопустимые значения индексов')
        return self.matrix[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        if not isinstance(row, int) or not isinstance(col, int):
            raise IndexError('недопустимые значения индексов')
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError('недопустимые значения индексов')
        self.matrix[row][col] = value

    def __add__(self, other):
        if type(other) in (int, float):
            result = [[self.matrix[i][j] + other for j in range(self.cols)] for i in range(self.rows)]
        elif not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            raise ValueError('операции возможны только с матрицами равных размеров')
        else:
            result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        elif isinstance(other, (int, float)):
            result = [[self.matrix[i][j] - other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        else:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __rsub__(self, other):
        return self.__sub__(other)



list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"