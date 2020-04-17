def int_func_word(string):
    return string.capitalize()


def int_func_words(string):
    words_list = string.split()
    result = []
    for i in words_list:
        result.append(int_func_word(i))
    return ' '.join(result)


print(int_func_word('text'))
print(int_func_words('text text text text text text '))