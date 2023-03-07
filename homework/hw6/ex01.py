# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input('Введите первый элемент прогрессии:'))
step = int(input('Введите шаг прогрессии: '))
count_elements = int(input('Введите количество элементов прогрессии: '))

my_list = [first_element]

for i in range(2, count_elements):
    my_list.append(first_element + (i - 1) * step)

print(my_list)
