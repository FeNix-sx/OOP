"""
Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это показано в примере:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)
Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.
"""
class NewList:
    def __init__(self, lst: list=[]) -> None:
        self.__lst = lst

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError("Необходимо задать список или класс NewList")

        reduced = [(item, type(item)) for item in self.__lst]
        if isinstance(other, NewList):
            deductible = [(item, type(item)) for item in other.__lst]
        else:
            deductible = [(item, type(item)) for item in other]

        for item in deductible:
            if item in reduced:
                reduced.remove(item)

        return NewList(list(map(lambda x: x[0], reduced)))

    def __rsub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError("Необходимо задать список или класс NewList")

        deductible = [(item, type(item)) for item in self.__lst]
        if isinstance(other, NewList):
            reduced = [(item, type(item)) for item in other.__lst]
        else:
            reduced = [(item, type(item)) for item in other]

        for item in deductible:
            if item in reduced:
                reduced.remove(item)

        return NewList(list(map(lambda x: x[0], reduced)))

    def get_list(self):
        return self.__lst


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])

res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
assert res_1.get_list() == [-4, 6, 10, 11, 15, False]

lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
assert lst1.get_list() == [-4, 6, 10, 11, 15, False]
print(lst1.get_list())

res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
print(res_2.get_list())
assert res_2.get_list() == [1, 2, 3]

res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
print(res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
lst = res_2.get_list() # [1, 2, 3]
print(lst)