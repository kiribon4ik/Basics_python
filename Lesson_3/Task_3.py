def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.pop(my_list.index(min(num_1, num_2, num_3)))
    print(sum(my_list))


my_func(1, 2, 3)
