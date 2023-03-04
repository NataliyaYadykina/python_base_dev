# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def my_pow(number, power):
    if power == 1:
        return number
    else:
        return number * my_pow(number, power - 1)

a = int(input('Какое число будем возводить в степень: '))
b = int(input('Введите степень: '))

print(my_pow(a, b))
