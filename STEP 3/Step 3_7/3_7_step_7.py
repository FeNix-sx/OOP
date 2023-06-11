"""
Подвиг 6 (релакс). Объявите класс Line, объекты которого создаются командой:

line = Line(x1, y1, x2, y2)
где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2). Могут быть произвольными числами. В объектах класса Line должны создаваться соответствующие локальные атрибуты с именами x1, y1, x2, y2.

В классе Line определить магический метод __len__() так, чтобы функция:

bool(line)
возвращала False, если длина линии меньше 1.

P.S. На экран ничего выводить не нужно. Только объявить класс.
"""
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 =x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return int(((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**(1/2))
