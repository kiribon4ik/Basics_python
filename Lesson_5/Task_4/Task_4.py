lines = [line.strip() for line in open('Input_task_4', encoding='utf-8')]
rus_num = ['Один', 'Два', 'Три', 'Четыре']
list_new = []
for i in range(len(lines)):
    tmp = lines[i].split()
    tmp.pop(0)
    tmp.insert(0, rus_num[i])
    tmp.append('\n')
    string = ' '.join(tmp)
    list_new.append(string)

with open('Output_task_4.txt', 'w', encoding='utf-8') as file:
    file.writelines(list_new)
