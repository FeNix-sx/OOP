"""
Подвиг 4. С помощью множественного наследования удобно описывать принадлежность
объектов к нескольким разным группам. Выполним такой пример.



Определите в программе классы в соответствии с их иерархией, представленной
на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку
на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive
с произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие
списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки.
На экран выводить ничего не нужно.
"""
class Digit:
    def __init__(self, value):
        super().__init__()
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        super().__setattr__(key, value)


class Integer(Digit):
    def __setattr__(self, key, value):
        if type(value) not in (int,):
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(key, value)


class Float(Digit):
    def __setattr__(self, key, value):
        if type(value) not in (float,):
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(key, value)


class Positive(Digit):
    def __setattr__(self, key, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(key, value)


class Negative(Digit):
    def __setattr__(self, key, value):
        if value >= 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(key, value)


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(2),
          PrimeNumber(5),
          PrimeNumber(19),
          FloatPositive(5.4),
          FloatPositive(15.3),
          FloatPositive(11.5),
          FloatPositive(2.4),
          FloatPositive(0.5)
          ]


lst_positive = list(filter(lambda item: isinstance(item, Positive), digits))
lst_float = list(filter(lambda item: isinstance(item, Float), digits))


print(len(lst_positive), lst_positive)
# test = Integer(1.0)
obj = Positive(11.0)
# d = Digit('1')
f = FloatPositive(-1.5)