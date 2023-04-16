"""
Подвиг 6. Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:

obj = AbstractClass()
переменная obj должна ссылаться на строку с содержимым:

"Ошибка: нельзя создавать объекты абстрактного класса"

P.S. В программе объявить только класс, выводить на экран ничего не нужно.
"""

class AbstractClass:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return "Ошибка: нельзя создавать объекты абстрактного класса"


obj = AbstractClass()
print(id(obj))
obj3 = AbstractClass()
print(id(obj3))