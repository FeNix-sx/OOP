"""
Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите два класса с именами:

Budget - для управления семейным бюджетом;
Item - пункт расходов бюджета.

Объекты класса Item должны создаваться командой:

it = Item(name, money)
где name - название статьи расхода; money - сумма расходов (вещественное или целое число).

Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с переданными значениями. Также с объектами класса Item должны выполняться следующие операторы:

s = it1 + it2 # сумма для двух статей расходов
и в общем случае:

s = it1 + it2 + ... + itN # сумма N статей расходов
При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих объектов класса Item.

Объекты класса Budget создаются командой:

my_budget = Budget()
А сам класс Budget должен иметь следующие методы:

add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).

Пример использования классов (эти строчки в программе писать не нужно):

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.
"""
from typing import Optional, Union, Type

class Item:
    def __init__(self, name: str=None, money: float=None) -> None:
        self.name = name
        self.money = money

    @staticmethod
    def __check_item(item: Union[int,float, Type['Item']]) -> float|int:
        if type(item) in (int, float):
            return item
        elif isinstance(item, Item):
            return item.money
        else:
            raise TypeError("Ошибка! Тип данных должен быть число или класс Item")

    def __add__(self, item: Union[int,float,Optional['Item']]) -> float|int:
        """ сложение двух классов или класса и числа """
        return self.__check_item(item) + self.money

    def __radd__(self, item: Union[int,float,Optional['Item']]) -> float|int:
        """ сложение двух классов или класса и числа (класс справа, второе слагаемое) """
        return self.__add__(item)



class Budget:
    def __init__(self) -> None:
        self.list_items = list()

    def add_item(self, it: Item) -> None:
        """ добавление статьи расхода в бюджет (it - объект класса Item) """
        self.list_items.append(it)

    def remove_item(self, indx: int) -> None:
        """ удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля) """
        if len(self.list_items) >= indx:
            del self.list_items[indx]

    def get_items(self) -> list:
        """ возвращает список всех статей расходов (список из объектов класса Item) """
        return self.list_items


name = ""
money = 0
it = Item(name, money)

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x