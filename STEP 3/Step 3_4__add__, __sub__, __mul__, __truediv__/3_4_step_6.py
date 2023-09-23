"""
Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:

lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа, остальные игнорировать (если указываются в списке). Например:

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть публичный атрибут:

lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

Также с объектами класса ListMath должны работать следующие операторы:

lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками, прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта (новый объект не создается).

P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.
"""
class ListMath:
    def __init__(self, lst: list=None) -> None:
        self.lst_math = [item for item in lst[:] if type(item) in (int, float)] if lst and type(lst) == list else []

    def get_lst(self):
        return self.lst_math

    @staticmethod
    def __check(other):
        if not isinstance(other, (int, float)):
            raise TypeError("Необходимо задать целое или вещественное число или класс NewList")

        if isinstance(other, ListMath):
            return other.lst_math

        return other

    def __add__(self, other):
        """
        Сложение каждого числа списка с определенным числом
        :param other:
        :return:
        """
        number = self.__check(other)
        return ListMath([item + number for item in self.lst_math])

    def __radd__(self, other):
        """
        Сложение каждого числа списка с определенным числом
        :param other:
        :return:
        """
        return self.__add__(self.__check(other))

    def __iadd__(self, other) -> None:
        """
        Сложение каждого числа списка с определенным числом
        :param other:
        :return:
        """
        number = self.__check(other)
        self.lst_math = [item + number for item in self.lst_math]
        return self

    def __sub__(self, other):
        """
        вычитание из каждого числа списка определенного числа
        :param other:
        :return:
        """
        number = self.__check(other)
        return ListMath([item - number for item in self.lst_math])

    def __rsub__(self, other):
        """
        вычитание из каждого числа списка определенного числа
        :param other:
        :return:
        """
        number = self.__check(other)
        return ListMath([number - item for item in self.lst_math])

    def __isub__(self, other) -> None:
        """
        вычитание из каждого числа списка определенного числа
        :param other:
        :return:
        """
        number = self.__check(other)
        self.lst_math = [item - number for item in self.lst_math]
        return self

    def __mul__(self, other):
        """
        умножение каждого числа списка на указанное число
        :param other:
        :return:
        """
        number = self.__check(other)
        return ListMath([number * item for item in self.lst_math])

    def __rmul__(self, other):
        """
        умножение каждого числа списка на указанное число
        :param other:
        :return:
        """
        return self.__mul__(self.__check(other))

    def __imul__(self, other):
        """
        умножение каждого числа списка на указанное число
        :param other:
        :return:
        """
        number = self.__check(other)
        self.lst_math = [item * number for item in self.lst_math]
        return self

    def __truediv__(self, other):
        """
        деление каждого числа списка на указанное число
        :param other:
        :return:
        """
        if other == 0:
            raise ZeroDivisionError("На ноль делить нельзя")

        number = self.__check(other)
        return ListMath([item/number for item in self.lst_math])

    def __rtruediv__(self, other):
        number = self.__check(other)
        return ListMath([number/item for item in self.lst_math if item != 0])

    def __itruediv__(self, other):
        """
        деление каждого числа списка на указанное число
        :param other:
        :return:
        """
        if other == 0:
            raise ZeroDivisionError("На ноль делить нельзя")

        number = self.__check(other)
        self.lst_math = [item/number for item in self.lst_math]
        return self


lst1 = ListMath()  # пустой список
lst2 = ListMath([1, 2, -5, 7.68])  # список с начальными значениями
lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
print(lst.get_lst())

lst = lst + 76 # сложение каждого числа списка с определенным числом
print(lst.get_lst())
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst.get_lst())
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0