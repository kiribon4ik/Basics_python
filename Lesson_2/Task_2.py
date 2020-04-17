start_list = []
result_list = []


def func(some_list):
    len_list = len(start_list)
    j = 0
    for r in range(0, len_list):
        x_list = some_list[(0 + j):(2 + j)]
        x_list.reverse()
        j += 2
        for res_num in x_list:
            result_list.append (res_num)


print('Создадим список')
n = int(input('Укажите числом количество элементов списка: '))
for i in range(1, (n + 1)):
    m = input(f'Введите {i} элемент списка: ')
    start_list.append(m)

print(f'Заданный список: {start_list}')

if len(start_list) % 2 == 0:
    func(start_list)
else:
    last = start_list.pop()
    func(start_list)
    result_list.append(last)
print(f'Преобразованный список: {result_list}')
