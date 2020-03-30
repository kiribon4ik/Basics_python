number = input('Введите любое число: ')

n = int(number)
numbers_list = []

for i in range(1, (n + 1)):
    numbers_list.append(int(number * i))

print(f'Сумма чисел равна: {sum(numbers_list)}')