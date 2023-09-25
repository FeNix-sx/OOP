"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0Jy6n9KESPE

Подвиг 9 (на повторение). Объявите в программе базовый класс с именем IteratorAttrs
для перебора всех локальных атрибутов объектов класса. Напомню, что для этого используются два магических метода:

__iter__() - для получения объекта-итератора (в данном случае - это сам объект self)
__next__() - для перебора локальных атрибутов объекта self (используйте для этого словарь __dict__)

Метод __next__() на каждой итерации должен возвращать кортеж в формате: (имя атрибута, значение).

Подсказка: здесь можно определить один метод __iter__() как функцию-генератор.

Объявите дочерний класс SmartPhone, объекты которого создаются командой:

phone = SmartPhone(model, size, memory)
где model - модель смартфона (строка); size - габариты (ширина, длина) в виде кортежа
двух чисел; memory - размер ОЗУ (памяти), как целое число. В каждом объекте класса
SmartPhone должны создаваться соответствующие локальные атрибуты: model, size, memory.

Благодаря наследованию от базового класса IteratorAttrs, с объектами класса SmartPhone
должен выполняться оператор for:

for attr, value in phone:
    print(attr, value)
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""
class IteratorAttrs:
    def __iter__(self):
        for item in self.__dict__.items():
            yield item


class SmartPhone(IteratorAttrs):
    def __init__(self, model:str, size:tuple, memory:int):
        self.model = model
        self.size = size
        self.memory = memory


model = "text"
size = (1, 2)
memory = 3
phone = SmartPhone(model, size, memory)

for attr, value in phone:
    print(attr, value)