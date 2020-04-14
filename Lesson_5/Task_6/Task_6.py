def modified_list(any_list):
    for el in any_list:
        while el.count('') != 0:
            el.pop(el.index(''))
    return any_list


if __name__ == '__main__':
    lines = [line.strip() for line in open('Study_plan.txt', encoding='utf-8')]
    lines = [el.split(' ') for el in lines]
    dict_lessons = {}

    for element in modified_list(lines):
        list_number = []
        for string in element[1:]:
            list_num_tmp = []
            for el in string:
                try:
                    num = int(el)
                    list_num_tmp.append(str(num))
                except ValueError:
                    continue
            number = ''.join(list_num_tmp)
            list_number.append(number)
        for elem in list_number:
            try:
                i = int(elem)
            except ValueError:
                list_number.remove(elem)
        list_number = list(map(int, list_number))
        dict_lessons.update({element[0].rstrip(':'): sum(list_number)})
    print(f'Dictionary example: {dict_lessons}')
