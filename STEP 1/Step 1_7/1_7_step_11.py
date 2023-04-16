"""
Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS.
В этом классе должны быть реализованы следующие методы:

add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным именем. 
Каждый объект класса Application должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.

P.S. В программе нужно только объявить классы с указанным функционалом.
"""
class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

class AppStore:
    katalog_list = list()

    @classmethod
    def add_application(cls, app: Application):
        """
        Добавление нового приложения app в магазин
        :param app: объект класса Application
        :return: None
        """
        cls.katalog_list.append(app)

    @classmethod
    def remove_application(cls, app: Application):
        """
        удаление приложения app из магазина
        :param app: объект класса Application
        :return: None
        """
        if app in cls.katalog_list:
            cls.katalog_list.remove(app)
        else:
            raise ValueError("Приложение отсутствует в каталоге!")

    @classmethod
    def block_application(cls, app: Application):
        """
        блокировка приложения app
        (устанавливает локальное свойство blocked объекта app в значение True)
        :param app: объект класса Application
        :return: None
        """
        if app in cls.katalog_list:
            cls.katalog_list[cls.katalog_list.index(app)].blocked = True
        else:
            raise ValueError("Невозможно разблокировать приложение! Приложение отсутствует в каталоге!")

    @classmethod
    def total_apps(cls):
        """
        Возвращает общее число приложений в магазине
        :return:
        """
        return len(cls.katalog_list)


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
# Здесь Application - класс, описывающий добавляемое приложение с указанным именем.
# Каждый объект класса Application должен содержать локальные свойства:

store = AppStore()
app_youtube = Application("Youtube")
assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"

store.add_application(app_youtube)
store.block_application(app_youtube)

assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"

app_stepik = Application("Stepik")
store.add_application(app_stepik)

assert store.total_apps() == 2, "неверное число приложений в магазине"

store.remove_application(app_youtube)
assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"