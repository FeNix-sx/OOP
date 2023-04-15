"""
Подвиг 4. Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model для
записи и считывания информации о модели автомобиля из локальной приватной переменной __model.

Объект-свойство объявите с помощью декоратора @property. Также в объекте-свойстве model должны
быть реализованы проверки:

- модель автомобиля - это строка;
- длина строки модели должна быть в диапазоне [2; 100].

Если проверка не проходит, то локальное свойство __model остается без изменений.

Объекты класса Car предполагается создавать командой:

car = Car()
и далее работа с объектом-свойством, например:

car.model = "Toyota"
P.S. В программе объявить только класс. На экран ничего выводить не нужно.
"""
class Car:
    def __init__(self):
        self.__model: str=""

    @staticmethod
    def __check_model(model):
        return type(model) == str and len(model) in range(2, 101)
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = [self.__model, model][self.__check_model(model)]


car = Car()
car.model = "Toyota"
print(car.model)