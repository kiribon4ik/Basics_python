str_list = []
string = input('Input some information or push Enter for quit: ')
while string != '':
    str_list.append(string + '\n')
    string = input('Input some information or push Enter for quit: ')

with open('Task_1.txt', 'w', encoding='utf-8') as file:
    file.writelines(str_list)

with open('Task_1.txt', encoding='utf-8') as file:
    print(f'File {file.name} contain the next information:\n{file.read()}')
