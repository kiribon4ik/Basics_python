string = input('Введите строку из нескольких слов, разделённых пробелом: ')
some_list = string.split()


def func(list):
    for k, i in enumerate(list, 1):
        print(k, i)


if len(some_list[1]) < 10:
    func(some_list)
else:
    word_2 = (some_list.pop())[:10]
    some_list.append(word_2)
    func(some_list)

