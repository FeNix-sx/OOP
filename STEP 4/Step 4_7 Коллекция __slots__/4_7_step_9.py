"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rtma49Ye7hY

Подвиг 7. Объявите класс Note (нота), объекты которого создаются командой:

note = Note(name, ton)
где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си);
ton - тональность ноты (целое число). Тональность (ton) принимает следующие целые значения:

-1 - бемоль (flat);
0 - обычная нота (normal);
1 - диез (sharp).

Если в названии (name) или тональности (ton) передаются недопустимые значения,
то генерируется исключение командой:
raise ValueError('недопустимое значение аргумента')

В каждом объекте класса Note должны формироваться локальные атрибуты
с именами _name и _ton с соответствующими значениями.

Объявите класс с именем Notes, в объектах которого разрешены только локальные
атрибуты с именами (ограничение задается через коллекцию __slots__):

_do - ссылка на ноту до (объект класса Note);
_re - ссылка на ноту ре (объект класса Note);
_mi - ссылка на ноту ми (объект класса Note);
_fa - ссылка на ноту фа (объект класса Note);
_solt - ссылка на ноту соль (объект класса Note);
_la - ссылка на ноту ля (объект класса Note);
_si - ссылка на ноту си (объект класса Note).

Объект класса Notes должен создаваться командой:

notes = Notes()
и быть только один (одновременно в программе два и более объектов класса Notes недопустимо).
Используйте для этого паттерн Singleton.

В момент создания объекта Notes должны автоматически создаваться перечисленные локальные
атрибуты и ссылаться на соответствующие объекты класса Note (тональность (ton) у всех нот
изначально равна 0).

Обеспечить возможность обращения к нотам по индексам: 0 - до; 1 - ре; ... ; 6 - си.
Например:
nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа

Если указывается недопустимый индекс (не целое число, или число, выходящее за интервал [0; 6]),
то генерируется исключение командой:
raise IndexError('недопустимый индекс')

Создайте в программе объект notes класса Notes.

P.S. В программе следует объявить только классы и создать объект notes. На экран выводить
ничего не нужно.
"""
class Note:
    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__ (self, key, value):
        if key == '_name' and value in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            return object.__setattr__(self, key, value)
        elif key == '_ton' and -1 <= value <= 1:
            return object.__setattr__(self, key, value)
        raise ValueError('недопустимое значение аргумента')

class Notes:
    __slots__ = (
        '_do',
        '_re',
        '_mi',
        '_fa',
        '_solt',
        '_la',
        '_si'
    )
    __isinstans = None
    def __new__(cls, *args, **kwargs):
        if not cls.__isinstans:
            cls.__isinstans = super().__new__(cls)
            return cls.__isinstans
        return cls.__isinstans

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note('ре', 0)
        self._mi = Note('ми', 0)
        self._fa = Note('фа', 0)
        self._solt = Note('соль', 0)
        self._la = Note('ля', 0)
        self._si = Note('си', 0)

    def __getitem__(self, item):
        notes = [
            self._do,
            self._re,
            self._mi,
            self._fa,
            self._solt,
            self._la,
            self._si
        ]
        getattr(self, self.__slots__[item])

        if -len(notes) <= item < len(notes):
            return notes[item]
        raise IndexError('недопустимый индекс')

    def __setitem__(self, key, value):
        print(key, value)


notes = Notes()
nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа
print(notes[3]._ton)