"""
Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:

dt = DeltaClock(clock1, clock2)
где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:

clock = Clock(hours, minutes, seconds)
где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
Если разность получается отрицательной, то разницу времен считать нулевой.

Пример использования классов (эти строчки в программе писать не нужно):

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
Обратите внимание, добавляется незначащий ноль, если число меньше 10.

P.S. На экран ничего выводить не нужно, только объявить классы.
"""

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = self.__chek_time(hours)
        self.minutes = self.__chek_time(minutes)
        self.seconds = self.__chek_time(seconds)

    @staticmethod
    def __chek_time(time: int) -> int:
        if type(time) == int and time >= 0:
            return time
        else:
            raise ValueError("Должно быть целым неотрицательным числом")

    def get_time(self) -> int:
        return self.hours*3600 + self.minutes*60 + self.seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2:Clock) -> None:
        self.__clock1 = clock1
        self.__clock2 = clock2

    def __str__(self) -> str:
        hours = 0 if self.__clock1.hours - self.__clock2.hours < 0 else self.__clock1.hours - self.__clock2.hours
        minutes = 0 if self.__clock1.minutes - self.__clock2.minutes < 0 else self.__clock1.minutes - self.__clock2.minutes
        seconds = 0 if self.__clock1.seconds - self.__clock2.seconds < 0 else self.__clock1.seconds - self.__clock2.seconds
        return f"{self._format(hours)}: {self._format(minutes)}: {self._format(seconds)}"

    @staticmethod
    def _format(time: int)->str:
        return str(time).rjust(2,"0")

    def __len__(self):
        return self.__clock1.get_time()-self.__clock2.get_time()



dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды

# Решение от бота
# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def get_time(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds
#
#
# class DeltaClock:
#     def __init__(self, clock1, clock2):
#         self.clock1 = clock1
#         self.clock2 = clock2
#         self.diff = self.clock1.get_time() - self.clock2.get_time()
#
#     def __str__(self):
#         hours = abs(self.diff) // 3600
#         minutes = (abs(self.diff) % 3600) // 60
#         seconds = abs(self.diff) % 60
#         if self.diff >= 0:
#             return f"{hours:02}: {minutes:02}: {seconds:02}"
#         else:
#             return "00: 00: 00"
#
#     def __len__(self):
#         return abs(self.diff)