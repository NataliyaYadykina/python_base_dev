# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

from random import randint

my_list = [randint(1, 5) for _ in range(10)]
print(my_list)
my_dict = {}

for i in my_list:
    my_dict[i] = my_dict.get(i, 0) + 1
    print(i if my_dict.get(i) == 1 else f'{i}_{my_dict.get(i) - 1}', end = ' ')
print('\n', f'{my_dict}')