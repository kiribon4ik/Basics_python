from itertools import count, cycle

count_list = []
# итератор, генерирующий список целых чисел, начиная с указанного
for i in count(start=3, step=1):
    if i > 10:
        break
    count_list.append(i)
print(count_list)

# итератор, повторяющий элементы ранее созданного списка
num_cycle = 0
for j in cycle(count_list):
    if num_cycle > 100:
        break
    num_cycle += 1
    print(j)
