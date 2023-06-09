"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PJsJOIxZOdM

Подвиг 6. Ваша задача написать программу поиска слова в строке. Задача усложняется тем, что слово должно определяться в разных его формах. Например, слово:

программирование

может иметь следующие формы:

программирование, программированию, программированием, программировании, программирования, программированиям, программированиями, программированиях

Для решения этой задачи необходимо объявить класс Morph (морфология), объекты которого создаются командой:

mw = Morph(word1, word2, ..., wordN)
где word1, word2, ..., wordN - возможные формы слова.

В классе Morph реализовать методы:

add_word(self, word) - добавление нового слова (если его нет в списке слов объекта класса Morph);
get_words(self) - получение кортежа форм слов.

Также с объектами класса Morph должны выполняться следующие операторы сравнения:

mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)
И аналогичная пара сравнений:

"word" == mw1
"word" != mw1
После создания класса Morph, формируется список dict_words из объектов этого класса, для следующих слов с их словоформами:

- связь, связи, связью, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях

Затем, прочитайте строку из входного потока командой:

lst_words = input()
Найдите все вхождения слов из списка dict_words (используя операторы сравнения) в строке lst_words (без учета регистра, знаков пунктуаций и их словоформы). Выведите на экран полученное число.
"""
class Morph:
    def __init__(self, *args):
        self.lst_words = list(args)

    def __eq__(self, word: str):
        return word.lower() in self.lst_words

    def add_word(self, word):
        '''добавление нового слова (если его нет в списке слов объекта класса Morph)'''
        if word not in self.lst_words:
            self.lst_words.append(word)

    def get_words(self):
        '''получение кортежа форм слов.'''
        return tuple(self.lst_words)


# dict_words = [
#     Morph(
#         'связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'
#     ),
#     Morph(
#         'формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'
#     ),
#     Morph(
#         'вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'
#     ),
#     Morph(
#         'эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'
#     ),
#     Morph(
#         'день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
#     )
# ]
#  or
s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]

mw = Morph('связь', 'связи', 'связью', 'связей')
# text = input()
text = "Мы будем устанавливать связь завтра днем."
text = [word.lower().strip(".,") for word in text.split()]
result = []

for t in text:
    result.append(sum([t == mw for mw in dict_words]))

print(sum(result))
