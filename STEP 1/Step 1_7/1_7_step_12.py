"""
Подвиг 11 (на повторение). Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:

add_message(msg) - добавление нового сообщения в список сообщений;
remove_message(msg) - удаление сообщения из списка;
set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
show_last_message(число) - отображение последних сообщений;
total_messages() - возвращает общее число сообщений.

Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:

lst_words - текст сообщения (строка);
fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в противном случае, изначально False);

P.S. Как хранить список сообщений, решите самостоятельно.
"""
class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    message_db = list()

    @classmethod
    def add_message(cls, msg):
        """
        добавление нового сообщения в список сообщений
        :return: None
        """
        cls.message_db.append(msg)

    @classmethod
    def remove_message(cls, msg):
        """
        удаление сообщения из списка
        :return: None
        """
        if msg in cls.message_db:
            cls.message_db.remove(msg)

    @classmethod
    def set_like(cls, msg):
        """
        поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like
        объекта msg: если лайка нет то он ставится, если уже есть, то убирается)
        :return:
        """
        cls.message_db[cls.message_db.index(msg)].fl_like = not cls.message_db[cls.message_db.index(msg)].fl_like

    @classmethod
    def show_last_message(cls, number: int):
        """
        отображение последних сообщений
        :return: None
        """
        print(cls.message_db[-number:])

    @classmethod
    def total_messages(cls):
        """
        возвращает общее число сообщений
        :return: число сообщений (int)
        """
        return len(cls.message_db)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)