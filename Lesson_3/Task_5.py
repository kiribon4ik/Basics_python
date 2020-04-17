sum_list = []
numbers_input = input('Чтобы получить сумму, введите числа через пробел, для выхода q: ')

while True:
    if numbers_input.find('q') == -1:
        numbers_list = numbers_input.split()
        for i in numbers_list:
            sum_list.append(float(i))
        print(f'Сумма введенных чисел равна: {sum(sum_list)}')
        numbers_input = input('Чтобы получить сумму, введите числа через пробел, для выхода q: ')
        continue
    else:
        numbers_list = numbers_input.split()
        numbers_list.remove('q')
        for i in numbers_list:
            sum_list.append(float(i))
        print(f'Сумма ранее введенных чисел равна: {sum(sum_list)}')
        break
