class Car:

    def __init__(self, speed=0, color=None, name=None, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name}, цвет {self.color} поехала')

    def stop(self):
        print(f'Машина {self.name}, цвет {self.color} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name}, цвет {self.color} повернула {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость - {self.speed} миль в час')


class TownCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил скорость!\n'
                  f'Текущая скорость {self.name} - {self.speed} миль в час')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} миль в час')


class SportCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, color, name, speed=0, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} превысил скорость!\n'
                  f'Текущая скорость {self.name} - {self.speed} миль в час')
        else:
            print(f'Текущая скорость {self.name} - {self.speed} миль в час')


class PoliceCar(Car):
    def __init__(self, color, name, speed=0, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar('зеленый', 'opel', speed=80)
town_car.go()
town_car.turn('налево')
town_car.show_speed()

sport_car = SportCar('красный', 'mazda')
sport_car.stop()
sport_car.show_speed()
print(sport_car.is_police)

work_car = WorkCar('серый', 'ЗИЛ')
work_car.go()
work_car.turn('направо')

police_car = PoliceCar('черный', 'Lada')
if police_car.is_police: print(f'Автомобль марки {police_car.name} - полицейский')
police_car.go()
police_car.turn('налево')
police_car.stop()
