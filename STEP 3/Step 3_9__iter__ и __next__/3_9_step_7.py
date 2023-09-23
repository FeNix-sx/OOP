"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wfy7UyTSN_Y

Подвиг 6. Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных) списков следующей структуры:

lst = [[x00],
       [x10, x11],
       [x20, x21, x22],
       [x30, x31, x32, x33],
       ...
      ]
Для этого необходимо в программе объявить класс с именем TriangleListIterator, объекты которого создаются командой:

it = TriangleListIterator(lst)
где lst - ссылка на перебираемый список.

Затем, с объектами класса TriangleListIterator должны быть доступны следующие операции:

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)
Итератор должен перебирать элементы списка по указанной треугольной форме. Даже если итератору на вход будет передан прямоугольная таблица (вложенный список), то ее перебор все равно должен осуществляться по треугольнику. Если же это невозможно (из-за структуры списка), то естественным образом должна возникать ошибка IndexError: index out of range (выход индекса за допустимый диапазон).

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""
class TriangleListIterator:
    def __init__(self, lst: list):
        self.lst = lst
        self.items = len(lst)
        self.res = list()
        self.__result()

    def __result(self):
        for i in range(self.items):
            for j in range(i+1):
                if j < len(self.lst[i]):
                    self.res.append(self.lst[i][j])

    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        self.indx += 1
        if self.indx < len(self.res):
            return self.res[self.indx]
        else:
            raise StopIteration


    # def __next__(self):
    #     self.index += 1
    #     if self.index >= len(self.lst):
    #         raise StopIteration
    #     if self.index < len(self.lst[self.index]):
    #         # res = [self.lst[self.index][i] for i in range(self.index+1)]
    #         return ", ".join(str(i) for i in self.lst[self.index][:self.index+1])
    #     else:
    #         raise IndexError("index out of range")


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33', 'cac']]

it = TriangleListIterator(lst)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)

ls = [['1'],
      [2, 3],
      [4, 5, 6],
      ['7', 8, '9', 10]]

ls_one = [x for row in ls for x in row]
t = TriangleListIterator(ls)
for i, x in enumerate(t):
    y = ls_one[i]
    z = x
    assert x == ls_one[i], "итератор вернул неверное значение"