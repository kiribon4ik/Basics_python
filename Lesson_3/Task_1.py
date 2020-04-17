def my_func(x, y):
    try:
        x = float(x)
        y = float(y)
        result = x / y
        return print(f'Результат деления {x} на {y} будет {round(result, 2)}')
    except ZeroDivisionError:
        print('Деление на ноль запрещено!!!')
    except ValueError:
        print('Введено не число!!!')


num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')
my_func(num_1, num_2)
