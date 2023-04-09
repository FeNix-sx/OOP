"""
Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price объектов класса Book;

Объекты класса Book предполагается создавать командой:

book = Book(автор, название, цена)
При этом, в каждом объекте должны создаваться приватные локальные свойства:

__author - строка с именем автора;
__title - строка с названием книги;
__price - целое число с ценой книги.

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.
"""
class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        """
        Запись в локальное приватное свойство __title объектов класса Book значения title
        :param title:
        """
        self.__title = title

    def set_author(self, author):
        """
        Запись в локальное приватное свойство __author объектов класса Book значения author
        :param author:
        """
        self.__author = author


    def set_price(self, price):
        """
        Запись в локальное приватное свойство __price объектов класса Book значения price
        :param price:
        """
        self.__price = price

    def get_title(self):
        """
        Получение значения локального приватного свойства __title объектов класса Book
        :return: self.__title
        """
        return self.__title

    def get_author(self):
        """
        Получение значения локального приватного свойства __author объектов класса Book
        :return: self.__author
        """
        return self.__author

    def get_price(self):
        """
        Получение значения локального приватного свойства __price объектов класса Book
        :return: self.__price
        """
        return self.__price