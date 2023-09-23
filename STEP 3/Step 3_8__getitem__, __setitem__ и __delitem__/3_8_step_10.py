"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/dFdXOJwMc0E

Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:

things = Bag(max_weight)
где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)
где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение). В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется исключение:

raise ValueError('превышен суммарный вес предметов')
Также с объектами класса Bag должны выполняться следующие команды:

t = things[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
things[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del things[indx] # удаление вещи из сумки, расположенной по индексу indx
Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')
Пример использования классов (эти строчки в программе не писать):

things = Bag(1000)
things.add_thing(Thing('книга', 100))
things.add_thing(Thing('носки', 200))
things.add_thing(Thing('рубашка', 500))
things.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(things[2].name) # рубашка
things[1] = Thing('платок', 100)
print(things[1].name) # платок
del things[0]
print(things[0].name) # платок
t = things[4] # генерируется исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""
class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.weight = 0
        self.things = list()

    def add_thing(self, thing):
        if isinstance(thing, Thing):
            if self.weight + thing.weight <= self.max_weight:
                self.things.append(thing)
                self.weight += thing.weight
            else:
                raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, item):
        if isinstance(item, int) and abs(item) < len(self.things):
            return self.things[item]
        raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if isinstance(key, int) and isinstance(value, Thing) and abs(key) < len(self.things):
            if self.weight - self.things[key].weight + value.weight <= self.max_weight:
                self.weight += value.weight - self.things[key].weight
                self.things[key] = value
            else:
                raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        if isinstance(key, int) and abs(key) < len(self.things):
            del self.things[key]


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError