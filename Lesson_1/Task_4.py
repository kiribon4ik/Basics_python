number = input('Введите целое положительное число: ')

while True:
    if number.isdigit() != True or int(number) < 0:
        number = input('Введите целое положительное число: ')
    else:
        number = list(number)
        break

print(f'Самая большая цифра в введеном числе {max(number)}')
