# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def is_simple_number(number):
    i = 2
    while i <= number // 2:
        if not number % i and i != number:
            print('Not simple.')
            break
        i += 1
    else:
        print('Simple.')

number = int(input('Enter number: '))

is_simple_number(number)