"""
Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:

el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(x1, y1, x2, y2)
где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла. Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.

В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты x1, y1, x2, y2 существуют и False - в противном случае.

Также в классе Ellipse нужно реализовать метод:

get_coords() - для получения кортежа текущих координат объекта.

Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать исключение командой:

raise AttributeError('нет координат для извлечения')
Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. Два объекта должны быть созданы командой

Ellipse()
и еще два - командой:

Ellipse(x1, y1, x2, y2)
Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2. (Помните, что для этого был определен магический метод __bool__()).

P.S. На экран ничего выводить не нужно.
"""
class SetCoord:
    def __set_name__(self, owner, name):
        self.name = "" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, value)


class Ellipse:
    x1 = SetCoord()
    y1 = SetCoord()
    x2 = SetCoord()
    y2 = SetCoord()

    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = self.get_coords()

    def __bool__(self):
        return all((self.x1, self.y1, self.x2, self.y2))

    def get_coords(self):
        if  self.__bool__():
            return (self.x1, self.y1, self.x2, self.y2)
        raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]

for item in lst_geom:
    if bool(item):
        item.get_coords()
