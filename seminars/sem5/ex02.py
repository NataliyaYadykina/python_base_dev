# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.

from random import randint

long_list = randint(10,25)
list_points = [randint(1,5) for _ in range(long_list)]
print(list_points)

min_point = min(list_points)
max_point = max(list_points)
print(min_point, max_point)

for i in range(len(list_points)):
    if list_points[i] == max_point:
        list_points[i] = min_point

print(list_points)
