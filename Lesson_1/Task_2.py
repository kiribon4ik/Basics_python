sec = int(input('Введите время в секундах: '))

if (sec / 60) >= 60:
    hours = sec // 3600
    minutes = sec % 3600 // 60
    seconds = sec % 3600 % 60
else:
    hours = sec // 3600
    minutes = sec // 60
    seconds = sec % 3600 % 60

print("%02i:%02i:%02i" % (hours, minutes, seconds))