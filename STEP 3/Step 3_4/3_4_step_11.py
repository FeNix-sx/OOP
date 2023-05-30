"""
Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:



 Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):



Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

mp = MaxPooling(step=(2, 2), size=(2,2))
где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)
где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")
Пример использования класса (эти строчки в программе писать не нужно):

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
Результатом будет таблица чисел:

6 8
9 7

P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно.
"""
class MaxPooling:
    def __init__(self, step: tuple=(2, 2), size: tuple=(2,2)) -> None:
        self.step = step
        self.size = size

    @staticmethod
    def __check_matrix(matrix: list) -> None:
        row = len(matrix[0])
        for column in matrix:
            if row != len(column) or False in [isinstance(item, (float, int)) for item in column]:
                raise ValueError("Неверный формат для первого параметра matrix.")

    def __call__(self, matrix, *args, **kwargs):
        self.__check_matrix(matrix)
        temp_matrix = [[0 for i in range(self.size[0])]for _ in range(self.size[1])]
        row, colunm = len(matrix), len(matrix[0])
        result, max_list = list(), list()
        r_start, c_start = 0, 0

        while True:
            if r_start >= colunm:
                break
            for r in range(self.step[0]):
                for c in range(self.step[1]):
                    temp_matrix[r][c] = matrix[r_start+r][c_start+c]

            max_list.append(max(max(item) for item in temp_matrix))
            c_start += self.step[0]
            if row - c_start >= self.step[0]:
                continue
            result.append(max_list)
            r_start += self.step[0]
            c_start, matrix = 0, list()




mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]