def my_func_1(x, y):
    result = x ** y
    return result


def my_func_2(x, y):
    result = pow(x, y)
    return result


def my_func_3(x, y):
    result = [x]
    if num_2 < 0:
        for i in range(1, y, -1):
            count = result.pop()
            result.insert(0, (count / x))
    elif y == 0:
        result = [1]
    else:
        for i in range(1, y, 1):
            count = result.pop()
            result.insert(0, (count * x))
    return result[0]


num_1 = int(input('Введите число для возведения в степень: '))
num_2 = int(input('Введите показатель степени: '))

print(f'Результат с использованием **: {my_func_1(num_1, num_2)}')
print(f'Результат с использованием pow: {my_func_2(num_1, num_2)}')
print(f'Результат с использованием собственной функции: {my_func_3(num_1, num_2)}')
