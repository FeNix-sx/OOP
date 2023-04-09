"""
Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах.
Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX,
где X - любая цифра (от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если
имя записано верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и
цифрами. Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и
check_name (декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""
from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    # CHARS_FOR_NUMBER = digits

    @staticmethod
    def check_card_number(number: str):
        list_number = number.split("-")
        valid = lambda x: len(x) == 4 and x.isdigit()
        return all([all(map(valid, list_number)), len(list_number) == 4])

        # if len(list_number) != 4:
        #     valid = lambda x: len(x)!= 4 or not x.isdigit()
        #     all([map(valid, list_number),len(list_number) != 4])
        # else:
        #     for num in list_number:
        #         if len(num) != 4 or not num.isdigit():
        #             return False
        #
        # return True

    @classmethod
    def check_name(cls, name: str):
        l_name = name.split()
        valid = lambda x: set(x) <= set(cls.CHARS_FOR_NAME)
        return all([all(map(valid, l_name)), len(l_name) == 2])
            # return all([set(nam)<=set(cls.CHARS_FOR_NAME) for nam in name.split()])


is_number = CardCheck.check_card_number("1238-5678-9012-0007")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_number)
print(is_name)