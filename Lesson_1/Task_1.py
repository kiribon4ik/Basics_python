word = input('Введите любое слово: ')
print(f'Вы ввели слово: {word}. Тип введенных данных: {type(word)}')

num = input(f'Введите число: ')
num_int = int(num)
num_float = float(num)
print(f'Вы ввели число со зачением {num}. Тип введенных данных: {type(num)}')
print(f'Преобразовав в целое число, тип изменится на {type(num_int)} со значением {num_int}')
print(f'Преобразовав в число c плавающей запятой, тип изменится на {type(num_float)} со значением {num_int:.2f}')