# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод:
# 2

from random import randint as ri

long1 = ri(8, 16)

list1 = [ri(1,10) for _ in range(long1)]
print(list1)
set_list1 = set(list1)
print(set_list1)

count = 0
for i in set_list1:
    count += list1.count(i) // 2
print(count)
