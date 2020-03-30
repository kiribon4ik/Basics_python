a = int(input('Введите дистацию в км, которую вы преодолели последний раз: '))
b = int(input('Укажите дистацию в км, которую вы желаете преодолеть: '))
i = 1
dist = []


def result(x, y, z):
    while True:
        if x <= b:
            x *= 1.1
            dist.append(x)
            print(f'{z}-ый день: {x:.2f}')
            z += 1
        elif x >= y:
            print(f'Ответ: на {z} день спортсмен достигнет результата - не менее {y} км')
            break


print('Результат:')
if a != 0:
    result(a, b, i)
elif a == 0:
    print('Рекомендуем Вам начать с дистанции 1 км')
    a = 1
    result(a, b, i)
