import random

num_list = [(str(random.randint(1, 10)) + ' ') for num in range(10)]

with open('Task_5.txt', 'w') as file:
    file.writelines(num_list)

with open('Task_5.txt') as file:
    input_list = list(map(int, (file.read().strip().split(' '))))
    list_sum = sum(input_list)
    print(f'Sum of number: {list_sum}')
