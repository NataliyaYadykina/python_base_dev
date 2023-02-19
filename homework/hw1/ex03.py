# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket_number = int(input('Введите номер билета: '))

left_sum = ticket_number // 100000 + ticket_number // 10000 % 10 + ticket_number // 1000 % 10
right_sum = ticket_number // 100 % 10 + ticket_number // 10 % 10 + ticket_number % 10

if left_sum == right_sum:
    print(f'{left_sum} = {right_sum} - билет счастливый.')
else:
    print(f'{left_sum} не равно {right_sum} - билет не счастливый.')