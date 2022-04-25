# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, 
# взятых из трёх заданных списков.
# Условие задачи
# 
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# 
# Техническое задание
# 
# Функция должна вернуть список строк-шуток.
# Функция принимает 4 параметра: количество шуток и 3 списка со словами.
# В списках nouns, adverbs, adjectives не обязательно одинакое количество элементов. Они могут быть произвольной длины.
# Проверьте работу функции для количества шуток больше, чем длины списков слов и меньше.
# Сделайте вызов функции как с позиционными аргументами, так и с именованными.
# Менять исходные списки nouns, adverbs, adjectives нельзя. Это «side effects»
# Документируйте код функции.

import random
# Cоставные части шуток по ТЗ

actors = ["автомобиль", "лес", "огонь", "город", "дом"]
setups = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
punchlines = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# Составные части шуток для генерации анекдотов категории Б

# actors = ["Медведь", "Мужик", "Петька", "Мусятник", "Улитка"]
# setups = ["надел шляпу", "сел в горящую машину", "задал вопрос Васильевичу", "купи слона", "заходит в бар"]
# punchlines = ["а она ему как раз", "и сгорел", "но есть один нюанс", "а ты возьми и купи слона", "возвращается через неделю и говорит: зачем ты это сделал?"]
def get_jokes(count, actors, setups, punchlines):
    """ Generate selected number of perfect 'category b' jokes from components in 3 different lists """
    actors = actors[:]
    setups = setups[:]
    punchlines = punchlines[:]
    list_of_jokes = []
    i = 0
    while i is not count:
        text = f'{random.choice(actors)} {random.choice(setups)} {random.choice(punchlines)}'
        list_of_jokes.append(text)
        i += 1
    return list_of_jokes
list_for_ready_jokes = (get_jokes(10, actors, setups, punchlines))
for element in list_for_ready_jokes:
    print(element)
