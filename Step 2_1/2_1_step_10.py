"""
Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python),
когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:

Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:

add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:

head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:

__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.

Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:

set_next(self, obj) - изменение приватного свойства __next на значение obj;
set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
get_next(self) - получение значения приватного свойства __next;
get_prev(self) - получение значения приватного свойства __prev;
set_data(self, data) - изменение приватного свойства __data на значение data;
get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:

ob = ObjList("данные 1")
А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
Объявите в программе классы LinkedList и ObjList в соответствии с заданием.

P.S. На экран ничего выводить не нужно.
"""
class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data: str = data

    def set_next(self, obj):
        """
        изменение приватного свойства __next на значение obj
        :param obj:
        """
        self.__next = obj

    def set_prev(self, obj):
        """
        изменение приватного свойства __prev на значение obj
        :param obj:
        """
        self.__prev = obj

    def get_next(self):
        """
        получение значения приватного свойства __next
        :return:
        """
        return self.__next

    def get_prev(self):
        """
        получение значения приватного свойства __prev
        :return:
        """
        return self.__prev

    def set_data(self, data):
        """
        изменение приватного свойства __data на значение data
        :param data:
        :return:
        """
        self.__data = data

    def get_data(self):
        """
        получение значения приватного свойства __data
        :return:
        """
        return self.__data


class LinkedList:
    def __init__(self):
        self.__data = list()
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        """
        Добавление нового объекта obj класса ObjList в конец связного списка
        :param obj:
        """
        if len(self.__data) >=1:
            self.__data.append(obj)
            self.__data[-2].set_next(obj)
            self.__data[-1].set_prev(self.__data[-2])
            self.tail = self.__data[-1]
        else:
            self.__data.append(obj)
            self.head = self.__data[0]
            self.tail = self.__data[-1]

    def remove_obj(self):
        """
        Удаление последнего объекта из связного списка
        """
        if len(self.__data) > 1:
            self.__data.pop(-1)
            self.__data[-1].set_next(None)
            self.tail = self.__data[-1]
        elif len(self.__data) == 1:
            self.__data.pop(-1)
            self.__data[-1].set_next(None)
            self.head = None
            self.tail = None
        else:
            raise IndexError("В списке нет элементов")

    def get_data(self):
        """
        получение списка из строк локального свойства __data всех объектов связного списка
        :return:
        """
        return [obj.get_data() for obj in self.__data]


# ob = ObjList("данные 1")
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
#
# print(lst.get_data())
# lst.remove_obj()
# print(lst.get_data())

ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
assert ls.get_data() == ['данные 1', 'данные 2', 'данные 3', 'данные 34'], "метод get_data вернул неверные данные"

ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
assert ls_one.get_data() == [1], "метод get_data вернул неверные данные"

h = ls_one.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 1, "неверное число объектов в списке: возможно некорректно работает метод add_obj"