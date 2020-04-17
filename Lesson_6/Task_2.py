class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass = (self._length * self._width * 25 * 5) / 1000
        return print(
            f'Длина дороги - {self._length} м, ширина - {self._width} м, масса асфальта - {mass} тонн')


road_mass = Road(5000, 20)
road_mass.mass()
