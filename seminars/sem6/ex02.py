# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

from random import randint as ri

long1 = ri(5, 10)

list1 = [ri(1,30) for _ in range(long1)]
print(list1)

count = 0
temp_list = []
for i in range(-1, long1 - 1):
    if list1[i-1] < list1[i] > list1[i+1]:
        temp_list.append(list1[i])
        count += 1
print(temp_list, '\ncount = ', count)
