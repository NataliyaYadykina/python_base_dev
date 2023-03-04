# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibbonachi(fib):
    if fib == 1:
        return 1
    elif fib == 0:
        return 0
    else:
        return fibbonachi(fib - 1) + fibbonachi(fib - 2)

number = int(input('Enter index of fibo number: '))

print(fibbonachi(number))
