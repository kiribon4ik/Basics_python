class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки инструментом {Pen.__name__} с названием {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки инструментом {Pencil.__name__} с названием {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки инструментом {Handle.__name__} с названием {self.title}')


stationery = Stationery()
stationery.draw()

pen = Pen('простой карандаш')
pen.draw()

pencil = Pencil('шариковая ручка')
pencil.draw()

handle = Handle('маркер')
handle.draw()
