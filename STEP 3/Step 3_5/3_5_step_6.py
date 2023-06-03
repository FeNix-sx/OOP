"""
Подвиг 5. Имеется стихотворение, представленное следующим списком строк:


Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова и разбить строку по
словам (слова разделяются одним или несколькими пробелами). На основе полученного списка слов, создать объект
класса StringText командой:

st = StringText(lst_words)
где lst_words - список из слов одной строчки стихотворения.

С объектами класса StringText должны быть реализованы операторы сравнения:

st1 > st2   # True, если число слов в st1 больше, чем в st2
st1 >= st2  # True, если число слов в st1 больше или равно st2
st1 < st2   # True, если число слов в st1 меньше, чем в st2
st1 <= st2  # True, если число слов в st1 меньше или равно st2

Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text. Затем, сформировать
новый список lst_text_sorted из отсортированных объектов класса StringText по убыванию числа слов. Для сортировки
использовать стандартную функцию sorted() языка Python. После этого преобразовать данный список (lst_text_sorted)
в список из строк (объекты заменяются на соответствующие строки, между словами ставится пробел).

P.S. На экран в программе ничего выводить не нужно.
"""
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__(self, lst_words):
        self.text = [word.strip("-?!,.;") for word in lst_words if word not in "-?–!,.;"]

    def __len__(self):
        return len(self.text)

    def __lt__(self, other):
        """меньше"""
        if isinstance(other, StringText):
            return len(self) < len(other)
        else:
            raise TypeError("Не верный тип данных!")

    def __le__(self, other):
        """меньше или равно"""
        if isinstance(other, StringText):
            return len(self) <= len(other)
        else:
            raise TypeError("Не верный тип данных!")


lst_text = [StringText(words.split()) for words in stich]
lst_text_sorted = sorted(lst_text, key=len, reverse=True)
lst_text_sorted = [" ".join(lst.text) for lst in lst_text_sorted]

# TEST-TASK___________________________________
assert all([[True if i in _ else False for i in "–?!,.;"] for _ in stich]), \
    "в stich есть знаки которые нужно удалить - (–?!,.;)"
assert len(lst_text) == 7 and all(
    True if isinstance(_, StringText) else False for _ in lst_text), "ошибка в lst_text"

assert lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1], "метод > работает неверно"
assert lst_text[1] < lst_text[4], "метод < работает неверно"

assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

print(lst_text_sorted == ['Я к вам пишу чего же боле',
                           'Теперь я знаю в вашей воле',
                           'Но вы к моей несчастной доле',
                           'Что я могу еще сказать',
                           'Хоть каплю жалости храня',
                           'Вы не оставите меня',
                           'Меня презреньем наказать'])

assert lst_text_sorted == ['Я к вам пишу чего же боле',
                           'Теперь я знаю в вашей воле',
                           'Но вы к моей несчастной доле',
                           'Что я могу еще сказать',
                           'Хоть каплю жалости храня',
                           'Вы не оставите меня',
                           'Меня презреньем наказать'], "неверно отсортирован список lst_text_sorted"

print("Правильный ответ.")
# st1 > st2   # True, если число слов в st1 больше, чем в st2
# st1 >= st2  # True, если число слов в st1 больше или равно st2
# st1 < st2   # True, если число слов в st1 меньше, чем в st2
# st1 <= st2  # True, если число слов в st1 меньше или равно st2