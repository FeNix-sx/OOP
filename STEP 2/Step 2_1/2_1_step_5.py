"""
Подвиг 4. Объявите класс с именем Money и определите в нем следующие переменные и методы:

- приватная локальная переменная money (целочисленная) для хранения количества денег
    (своя для каждого объекта класса Money);
- публичный метод set_money(money) для передачи нового значения приватной локальной переменной
    money (изменение выполняется только если метод check_money(money) возвращает значение True);
- публичный метод get_money() для получения текущего объема средств (денег);
- публичный метод add_money(mn) для прибавления средств из объекта mn класса Money к средствам текущего объекта;
- приватный метод класса check_money(money) для проверки корректности объема средств в параметре
    money (возвращает True, если значение корректно и False - в противном случае).

Проверка корректности выполняется по критерию: параметр money должен быть целым числом, больше или равным нулю.

Пример использования класса Money (эти строчки в программе не писать):

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
"""
class Money :
    def __init__(self, money=0):
        # private
        self.__money = money
    @staticmethod
    def __check_money(money):
        """
        Проверка корректности
        :param money:
        :return: bool
        """
        return 0 <= money and type(money) == int

    def set_money(self, money):
        """
        Передачи нового значения приватной локальной переменной money
        :param money:
        """
        self.__money = [self.__money, money][self.__check_money(money)]

    def get_money(self):
        """
        Получение текущего объема средств
        :return: int
        """
        return self.__money

    def add_money(self, mn):
        """
        Прибавление средств из объекта mn класса Money к средствам текущего объекта
        :param mn:
        """
        self.__money += mn.get_money()


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120

print(m1, m2)