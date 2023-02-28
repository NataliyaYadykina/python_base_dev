# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint

long = randint(15, 25)
my_list = [randint(1, 30) for _ in range(long)]
print(my_list)

number = int(input('Введите число: '))
found_number = my_list[0]
diff_min = abs(number - my_list[0])

if number in my_list:
    print(f'Число {number} встречается в списке {my_list.count(number)} раз.')
else:
    for value in my_list:
        if diff_min > abs(value - number):
            diff_min = abs(value - number)
            found_number = value
    print(f'Наиболее близкое по значению к искомому числу: {found_number}. Оно встречается в списке {my_list.count(found_number)} раз.')
