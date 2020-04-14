list_str = [line.strip() for line in open('Task_2.txt', encoding='utf-8')]
print(f'Count of string in file: {len(list_str)}')
for num, el in enumerate(list_str, 1):
    print(f'Count of words in string {num}: {len(el.split())}')
