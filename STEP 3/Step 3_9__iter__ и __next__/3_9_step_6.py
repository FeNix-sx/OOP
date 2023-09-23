"""
Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)
где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); salary - зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')
Пример использования класса (эти строчки в программе не писать):

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""
class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.person = [fio, job, old, salary, year_job]

        self.start = 0
        self.stop = len(self.person)
        self.step = 1

    def __getitem__(self, indx):
        if isinstance(indx, int) and abs(indx) < len(self.person):
            return self.person[indx]
        raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if isinstance(key, int) and abs(key) < len(self.person):
            self.person[key] = value
            self.fio, self.job, self.old, self.salary, self.year_job = self.person
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.current = self.start - self.step
        return self

    def __next__(self):
        if self.current + self.step < self.stop:
            self.current += self.step
            return self.person[self.current]
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
# pers[5] = 123 # IndexError