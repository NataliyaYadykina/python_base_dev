# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
count_tree = int(input('Введите количество кустов на грядке: '))
row = [randint(10, 30) for _ in range(count_tree)]
print(row)

max = row[len(row) - 2] + row[len(row) - 1] + row[0]
list_tree = [len(row) - 2, len(row) - 1, 0]
if row[len(row) - 2] + row[len(row) - 1] + row[0] < row[len(row) - 1] + row[0] + row[1]:
    max = row[len(row) - 1] + row[0] + row[1]
    list_tree = [len(row) - 1, 0, 1]
print(row[len(row) - 2] + row[len(row) - 1] + row[0], row[len(row) - 1] + row[0] + row[1])

for i in range(len(row) - 2):
    if row[i] + row[i + 1] + row[i + 2] > max:
        max = row[i] + row[i + 1] + row[i + 2]
        list_tree = [i, i + 1, i + 2]
    print(i, row[i] + row[i + 1] + row[i + 2])

print(f'Максимальное количество ягод за один заход: {max} с кустов под номерами {list_tree}.')
