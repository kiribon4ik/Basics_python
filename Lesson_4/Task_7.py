from itertools import count
from functools import reduce


def fact(n):
    for i in count(start=1, step=1):
        if i <= n:
            yield i
        else:
            break


num = int(input('Введите число: '))
print(f'Факториал числа {num} равен {reduce (lambda a, b: a * b, fact (num))}')
