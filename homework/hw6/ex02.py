# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint as ri

min_range = int(input('Введите минимальное значение диапазона: '))
max_range = int(input('Введите максимальное значение диапазона: '))

len_list = ri(15, 35)
my_list = [ri(1, 50) for _ in range(len_list)]
print(my_list)

list_index = []
for i in range(len_list):
    if min_range < my_list[i] < max_range:
        list_index.append(i)

print(list_index)
