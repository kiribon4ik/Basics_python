import time

color_input = ['красный', 'желтый', 'зеленый']


class TrafficLight:
    __color = color_input

    def running(self):
        if TrafficLight.__color[0] == 'красный' and TrafficLight.__color[2] == 'зеленый':
            for color in TrafficLight.__color:
                if color == 'красный':
                    print('\r', end='')
                    print(color, end='')
                    time.sleep(7)
                elif color == 'желтый':
                    print('\r', end='')
                    print(color, end='')
                    time.sleep(2)
                else:
                    print('\r', end='')
                    print(color, end='')
                    time.sleep(1)
        else:
            print('Ошибка цвета!!!')


traffic_light = TrafficLight()
traffic_light.running()
