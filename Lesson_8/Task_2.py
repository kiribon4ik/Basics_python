class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = int(input('Введите делимое: '))
divider = int(input('Введите делитель: '))

try:
    if divider == 0:
        raise MyError('Деление на ноль запрещено!')

except MyError as error:
    print(error)
else:
    print(f'Результат деления: {dividend / divider}')
