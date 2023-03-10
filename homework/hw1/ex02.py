# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?.
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# 2x + 4x = 6x

count = int(input('Введите общее количество журавликов: '))

if count % 6 == 0:
    print(f'''Петя и Сережа сделали по {count//6} журавлика(ов).\nКатя сделала {4 * count//6} журавлика(ов).''')
else:
    print('Не может быть такого общего количества. Кто-то из детей обманывает.')
