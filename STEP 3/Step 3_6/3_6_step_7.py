"""
Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:

indx = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число: целое или вещественное).

Определите в этом классе магические методы:

__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
__eq__() - чтобы объекты с одинаковыми хэшами были равны.

Затем, из входного потока прочитайте строки командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Строки имеют следующий формат:

название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с именем shop_items. Ключами словаря должны выступать сами объекты, а значениями - список в формате:

[indx, total]

где indx - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами). Подумайте, как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.

P.S. На экран ничего выводить не нужно, только объявить класс и сформировать словарь.

Sample Input:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000
"""
import sys

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name.lower()
        self.weight = float(weight)
        self.price = float(price)

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        """равно"""
        if isinstance(other, ShopItem):
            return self.name == other.name and self.weight == other.weight and self.price == other.price
        raise TypeError(f"Ошибка! {type(other)}")


lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = [lst_in[0].split(":")[0]]
lst.extend(lst_in[0].split(":")[1].split())
item = lst_in[0]
func = lambda item: [item.split(":")[0]] + item.split(":")[1].split()

curr_lst = list(map(func, lst_in))

shop_items = dict()
for item in curr_lst:
    key = ShopItem(*item)
    shop_items[key] = [ShopItem(*item), list(shop_items.keys()).count(key) + 1]

it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"