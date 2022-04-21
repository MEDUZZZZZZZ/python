# 3. Дан список, содержащий искаженные данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита'].
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'

# Техническое задание
#
# Список может содержать произвольное количество элементов.
# Имя сотрудника - всегда последнее слова в строке. Может содержать заглавные или строчные буквы в любом порядке.
# В результате имя сотрудника пишется строчными буквами и первая буква - заглавная.
# Формат вывода результата:
# Привет, Игорь!
# Привет, Марина!
# Привет, Николай!
# Привет, Аэлита!
#
# Усложнение:
# Выполните условие задачи, но формат вывода включает и должность,
# например: "Привет, инженер-конструктор Игорь", "Привет, главный бухгалтер Марина!" и т.п.

persons = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for person in persons:
    personalities = person.split()
    person_name = personalities[-1].capitalize()
    profession = (' '.join(personalities[0:-1:1]))
    print(f'Привет,{profession} {person_name}!')
