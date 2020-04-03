number = int(input('Укажите число единиц товара, которое хотите внести в структуру: '))
product_structure = {}
structure_list = []
# TODO Сделать ввод характеристик пользователем
characteristics = ['Название', 'Стоимость', 'Количество', 'Единицы']
result_dict = {}

for i in range(1, (number + 1)):
    product_list = []
    product_structure = {}
    product = input(f'Введите название товара {i}: ')
    cost = int(input(f'Введите стоимость товара {product}: '))
    quantity = int(input(f'Введите количество товара {product}: '))
    units = input(f'Введите единицы количества товара {product}: ')
    product_structure.update({'Название': product, 'Стоимость': cost, 'Количество': quantity, 'Единицы': units})
    product_list.append(i)
    product_list.append(product_structure)
    structure_list.append (tuple (product_list))
    print('-' * 50)
print(f'Структура ваших товаров: \n {structure_list}')


def func_prod(characteristic, prod_list):
    product_dict = 0
    characteristic_list = []
    for element in prod_list:
        for k in element:
            product_dict = list(element)
            product_dict = product_dict[1]
            product_dict = product_dict[characteristic]
        characteristic_list.append(product_dict)
    return characteristic_list


for x in characteristics:
    result_dict.update({x: func_prod(x, structure_list)})
print(f'Структура для анализа товаров: \n {result_dict}')
