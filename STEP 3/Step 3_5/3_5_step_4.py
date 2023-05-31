"""
Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:

track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); max_speed - максимальная скорость на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:

add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:

track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2  # True, если длина пути для track1 больше, чем для track2
track1 < track2  # True, если длина пути для track1 меньше, чем для track2
И функция:

n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
Создайте два маршрута track1 и track2 с координатами:

1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.

P.S. На экран в программе ничего выводить не нужно.
"""

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.__max_speed = max_speed


class Track:
    def __init__(self, start_x=0, start_y=0):
        self.__sratr_x = start_x
        self.__sratr_y = start_y
        self.__track = tuple()

    @staticmethod
    def __check_type(other):
        if not isinstance(other, Track):
            raise TypeError("Не верный тип данных!")

    def __eq__(self, other):
        self.__check_type(other)
        return self.__get_distance() == other.__get_distance()


    def __gt__(self, other):
        self.__check_type(other)
        return self.__get_distance() > other.__get_distance()

    def __len__(self):
        return int(self.__get_distance())

    def __get_distance(self):
        distance = 0
        if self.__track:
            x_0, y_0 = self.__sratr_x, self.__sratr_y

            for segment in self.__track:
                x_1, y_1, = segment.to_x, segment.to_y
                distance += ((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2) ** (1 / 2)
                x_0, y_0 = x_1, y_1

            return float(distance)

    def add_track(self, tr: TrackLine):
        """ добавление линейного сегмента маршрута (следующей точки); """
        self.__track += (tr,)

    def get_tracks(self):
        """ получение кортежа из объектов класса TrackLine."""
        return self.__track


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

print(track1 == track2)  # маршруты равны, если равны их длины
print(track1 != track2)  # маршруты не равны, если не равны их длины
print(track1 > track2)  # True, если длина пути для track1 больше, чем для track2
print(track1 < track2)  # True, если длина пути для track1 меньше, чем для track2
 # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
print(res_eq)