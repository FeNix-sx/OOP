"""
Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно.
"""
class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __eq__(self, other):
        """равно"""
        if isinstance(other, Body):
            return self.ro * self.volume == other.ro * other.volume
        elif isinstance(other, (int, float)):
            return self.ro * self.volume == other

    def __gt__(self, other):
        """больше"""
        if isinstance(other, Body):
            return self.ro * self.volume >= other.ro * other.volume
        elif isinstance(other, (int, float)):
            return self.ro * self.volume >= other

    def __ge__(self, other):
        """больше или равно"""
        if isinstance(other, Body):
            return self.ro * self.volume >= other.ro * other.volume
        elif isinstance(other, (int, float)):
            return self.ro * self.volume >= other

    def __lt__(self, other):
        """меньше"""
        if isinstance(other, Body):
            return self.ro * self.volume < other.ro * other.volume
        elif isinstance(other, (int, float)):
            return self.ro * self.volume < other


# TEST-TASK___________________________________
a = Body('Lora', 10, 10)
b = Body('Dora', 20, 20)
assert hasattr(a, "name") and hasattr(a, "ro") and hasattr(a, "volume"), "ошибка в локальных атрибутах"
assert type(a.name) is str, "name может быть только строкой"
assert type(a.ro) in (int, float), "ro  должно быть int или float"
assert type(a.volume) in (int, float), "volume  должно быть int или float"
assert not a > b, "ошибка при сравнении объектов >"
assert a < b, "ошибка при сравнении объектов <"
assert 10 < a, "ошибка при сравнении число < объект"
assert not 10 > a, "ошибка при сравнении число > объект"
assert not a == 5, "ошибка при сравнении объект == число"
assert a != 5, "ошибка при сравнении объект != число"
print("Правильное решение.")