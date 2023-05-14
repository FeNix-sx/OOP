"""
Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:


Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)
где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно.
"""
class AttribbuteValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_ObjList__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

class ObjList:
    data = AttribbuteValue()
    prev = AttribbuteValue()
    next = AttribbuteValue()

    def __init__(self, data: str, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, head: ObjList=None, tail: ObjList=None):
        self.__linklist = []
        self.head = head
        self.tail = tail

    def __call__(self, indx: int, *args, **kwargs):
        if len(self.__linklist) >= indx:
            return self.__linklist[indx].data

    def __len__(self):
        return len(self.__linklist)

    def add_obj(self,obj:ObjList):
        if len(self.__linklist)>=1:
            self.__linklist[-1].next = obj
            obj.prev = self.__linklist[-1]
        else:
            self.head = obj

        self.__linklist.append(obj)
        self.tail = obj

    def remove_obj(self, indx):
        if len(self.__linklist) >= indx:
            if self.__linklist[-1] == self.__linklist[indx]:
                del self.__linklist[indx]

                if len(self.__linklist)>0:
                    self.tail = self.__linklist[-1]

            elif self.__linklist[0] == self.__linklist[indx]:
                del self.__linklist[indx]

                if len(self.__linklist)>0:
                    self.head = self.__linklist[0]

            else:
                del self.__linklist[indx]

        if not len(self.__linklist):
            self.head, self.tail = None, None

    def get_data(self):
        return [item.data for item in self.__linklist]


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev

ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"