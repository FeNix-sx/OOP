"""
Подвиг 7. Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:

Lib - для представления библиотеки в целом;
Book - для описания отдельной книги.

Объекты класса Book должны создаваться командой:

book = Book(title, author, year)
где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).

Объекты класса Lib создаются командой:

lib = Lib()
Каждый объект должен содержать локальный публичный атрибут:

book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.

Также объекты класса Lib должны работать со следующими операторами:

lib = lib + book # добавление новой книги в библиотеку
lib += book

lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx
При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.

Также с объектами класса Lib должна работать функция:

n = len(lib) # n - число книг
которая возвращает число книг в библиотеке.

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.
"""
class Book:         # book = Book(title, author, year)
    def __init__(self, title: str=None, author: str=None, year: int=None) -> None:
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = list()

    def __add__(self, book: Book):
        """
        добавление новой книги в библиотеку
        :param book:
        :return:
        """
        self.book_list.append(book)
        return self

    def __iadd__(self, book: Book) -> None:
        """
        Сложение каждого числа списка с определенным числом
        :param book:
        :return:
        """
        return self.__add__(book)

    def __sub__(self, book: Book):
        """
        удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
        :param book:
        :return:
        """
        if type(book) == type(Book()):
            if book in self.book_list:
                self.book_list.remove(book)
            else:
                raise ValueError("Такая книга отсутствует в библиотеке")
        elif type(book) == int:
            self.sub_index(book)
        return self

    def __isub__(self, book: Book) -> None:
        return self.__sub__(book)

    def __len__(self):
        return len(self.book_list)

    def sub_index(self, indx):
        """
        удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
        :param indx:
        :return:
        """
        if indx < len(self.book_list):
            del self.book_list[indx]


book = Book("title", "author", "year")
lib = Lib()
indx = 1
lib = lib + book # добавление новой книги в библиотеку
lib += book
print(len(lib))
lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book
print(len(lib))
lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx