"""
Подвиг 5. Объявите класс Animal (животное), объекты которого создаются командой:

an = Animal(name, kind, old)
где name - название животного (строка); kind - вид животного (строка); old - возраст (целое число).
В каждом объекте этого класса должны создаваться соответствующие приватные
атрибуты: __name, __kind, __old.

В классе Animal должны быть объявлены объекты-свойства для изменения и считывания
приватных атрибутов:

name - для работы с приватным атрибутом __name;
kind - для работы с приватным атрибутом __kind;
old - для работы с приватным атрибутом __old.

Создайте в программе список с именем animals, который содержит три объекта
класса Animal со следующими данными:

Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3

P.S. В программе нужно объявить только класс и создать список animals.
На экран выводить ничего не нужно.
"""

class Property:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        if instance is None:
            return property()
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Animal:
    name = Property()
    kind = Property()
    old = Property()

    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old


animals = [
    Animal("Васька", "дворовый кот",5),
    Animal("Рекс", "немецкая овчарка", 8),
    Animal("Кеша", "попугай", 3)
]