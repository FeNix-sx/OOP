"""
Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:



 Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):



Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

mp = MaxPooling(__step=(2, 2), __size=(2,2))
где __step - шаг смещения окна по горизонтали и вертикали; __size - размер окна по горизонтали и вертикали.

Параметры __step и __size по умолчанию должны принимать кортеж со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)
где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")
Пример использования класса (эти строчки в программе писать не нужно):

mp = MaxPooling(__step=(2, 2), __size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
Результатом будет таблица чисел:

6 8
9 7

P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно.
"""
class MaxPooling:
    def __init__(self, step: tuple=(2, 2), size: tuple=(2,2)) -> None:
        self.__step = step
        self.__size = size

    @staticmethod
    def __check_matrix(matrix: list) -> list:
        row = len(matrix[0])
        colunm = len(matrix[0]) if row > 0 else 0

        for column in matrix:
            if row != len(column) or False in [isinstance(item, (float, int)) for item in column]:
                raise ValueError("Неверный формат для первого параметра matrix.")

        return [row, colunm]

    def __call__(self, matrix, *args, **kwargs):
        row, colunm = self.__check_matrix(matrix)
        temp_matrix = [[0 for i in range(self.__size[0])] for _ in range(self.__size[1])]
        r_step, c_step = self.__step[0], self.__step[1]

        if row == 0:
            return []

        result, max_list = list(), list()
        r_start, c_start = 0, 0

        while True:
            if row - r_start < self.__size[0]:
                break
            for r in range(self.__size[0]):
                for c in range(self.__size[1]):
                    temp_matrix[r][c] = matrix[r_start+r][c_start+c]

            max_list.append(max(max(item) for item  in temp_matrix))
            c_start += c_step

            if colunm - c_start >= self.__size[1]:
                continue

            r_start += r_step
            result.append(max_list)
            c_start, max_list = 0, list()

        return result



mp = MaxPooling(step=(2, 2), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(res)