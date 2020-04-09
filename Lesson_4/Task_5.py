from functools import reduce

new_list = [el for el in range(100, 1002, 2)]

print(new_list)
print(reduce(lambda a, b: a * b, new_list))
