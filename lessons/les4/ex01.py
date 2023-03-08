def f(x):
    return x*x

a = f # переменная а хранит в себе ссылку на функцию f
print(a(5))