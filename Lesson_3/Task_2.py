def func_user(**kwargs):
    result_list = []
    for i in kwargs.values():
        result_list.append(i)
    print(' '.join(result_list))


name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
date = input('Введите ваш год рождения: ')
city = input('В каком городе вы проживаете: ')
phone = input('Введите ваш номер телефона: ')
email = input('Введите ваш e-mail: ')

func_user(name=name, surname=surname, date=date, city=city, phone=phone, email=email)
