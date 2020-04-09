input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [input_list[(el + 1)] for el in range(len(input_list) - 1) if input_list[el] < input_list[(el + 1)]]
print(new_list)
