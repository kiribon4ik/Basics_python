my_list = [7, 5, 3, 3, 2]
print(f'Существующий набор натуральных чисел: {my_list}')


def add_number(number):
    my_list.append(number)
    my_list.sort()
    my_list.reverse()


while True:
    num = int(input('Введите любое натуральное число: '))
    if len(my_list) < 6:
        add_number(num)
    else:
        add_number(num)
        if num <= min(my_list):
            my_list.remove(max(my_list))
        else:
            my_list.remove(min(my_list))
    print(f'Список после добавления Вашего числа: {my_list}')
    next_step = input('Нажмите Enter для продолжения или введите нет для выхода ')
    if next_step.lower() == 'нет':
        break
    else:
        print (f'Последний набор натуральных чисел: {my_list}')
        continue
