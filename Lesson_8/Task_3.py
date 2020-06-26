class IntError(Exception):
    def __init__(self, txt=None):
        self.txt = txt

    @staticmethod
    def validator(some_el):
        try:
            some_num = int(some_el)
            return some_num
        except ValueError:
            print(IntError('Вы ввели не число!'))


input_data = input('Введите число: ')
input_list = []
while input_data != 'stop':
    if IntError.validator(input_data) != None:
        input_list.append(IntError.validator(input_data))
        input_data = input('Введите следующее число, для завершения stop: ')
    else:
        input_data = input('Повторите ввод, для завершения stop: ')
else:
    print(input_list)
