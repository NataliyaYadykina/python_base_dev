# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

from random import randint

long_list = randint(5, 10)
list1 = [randint(0, 10) for _ in range(long_list)]
print(list1)
long_list = randint(5, 10)
list2 = [randint(0, 10) for _ in range(long_list)]
print(list2)

result_list = list1 + list2
print(set(result_list))
