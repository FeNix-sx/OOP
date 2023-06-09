"""
Подвиг 9 (на повторение). Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:

things = Bag(max_weight)
где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).

В каждом объекте этого класса должен создаваться локальный приватный атрибут:

__things - список вещей в рюкзаке (изначально список пуст).

Сам же класс Bag должен иметь объект-свойство:

things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).

Также в классе Bag должны быть реализованы следующие методы:

add_thing(self, thing) - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
remove_thing(self, indx) - удаление предмета по индексу списка __things;
get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.

Каждая вещь описывается как объект класса Thing и создается командой:

t = Thing(название, вес)
где название - наименование предмета (строка); вес - вес предмета (целое или вещественное число).

В каждом объекте класса Thing должны формироваться локальные атрибуты:

name - наименование предмета;
weight - вес предмета.

Пример использования классов (эти строчки в программе писать не нужно):

things = Bag(1000)
things.add_thing(Thing("Книга по Python", 100))
things.add_thing(Thing("Котелок", 500))
things.add_thing(Thing("Спички", 20))
things.add_thing(Thing("Бумага", 100))
w = things.get_total_weight()
for t in things.things:
    print(f"{t.name}: {t.weight}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def __check_str(value):
        return value if type(value) == str else ""

    @staticmethod
    def __check_number(value):
        return value if type(value) in (int, float) else 0


class Bag:
    def __init__(self,max_weight):
        self.max_weight = max_weight
        self.__things = list()
    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        """
        добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight)
        не будет превышен, иначе добавление не происходит);
        :param thing:
        :return:
        """
        if thing.weight + self.get_total_weight() <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx: int):
        """
        удаление предмета по индексу списка __things
        """
        del self.__things[indx]

    def get_total_weight(self):
        """
        возвращает суммарный вес предметов в рюкзаке
        :return:
        """
        return sum(thing.weight for thing in self.__things)



bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
# print(things.things())
for t in bag.things:
    print(f"{t.name}: {t.weight}")