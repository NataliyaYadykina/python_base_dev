# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод:
# 3 3 2 12

from random import randint as ri

def print_uniq_nums(list1, list2):
    new_list = []
    for i in list1:
        if i not in list2:
            new_list.append(i)
    return new_list

long1 = ri(5, 10)
long2 = ri(5, 10)

list1 = [ri(1,30) for _ in range(long1)]
print(list1)
list2 = [ri(1,30) for _ in range(long2)]
print(list2)

new_list = print_uniq_nums(list1, list2)
if not new_list:
    print('Все элементы повторяются.')
