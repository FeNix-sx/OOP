"""
Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""

import random
from string import ascii_lowercase, digits
class EmailValidator:

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __email_part(n):
        len_email = random.randint(1, n)
        email = ""
        i = 1
        while i <= len_email:
            email += random.choice(ascii_lowercase + digits + "._")
            i += 1

        return email

    @staticmethod
    def __is_email_str(email):
        """
        для проверки типа переменной email, если строка, то возвращается значение True, иначе - False
        :return: bool
        """
        return type(email) == str

    @classmethod
    def get_random_email(cls):
        """
        для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
        где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка)
        :return:
        """
        email = f"{cls.__email_part(100)}@{cls.__email_part(45)}.{cls.__email_part(5)}"
        return email

    @classmethod
    def check_email(cls, email: str):
        """
        возвращает True, если email записан верно и False - в противном случае
        :param email:
        :return: bool
        """
        if cls.__is_email_str(email):
            email_list = email.split("@")

            if all([len(email_list) == 2, len(email_list[0]) <= 100, len(email_list[-1]) <= 50]):

                if "." in email_list[1] and ".." not in email_list[1] and ".." not in email_list[0]:

                    return all([set(text) <= set(ascii_lowercase + digits + "._") for text in email.split("@")])

                else:
                    return False
            else:
                return False
        else:
            return False


em = EmailValidator() # None
print(em)
res = EmailValidator.check_email("sc_lib@list.ru") # True
print(res)
res = EmailValidator.check_email("sc_lib@list_ru") # False
print(res)

assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False
email = EmailValidator.get_random_email()
print(email)
print(EmailValidator.check_email(email))