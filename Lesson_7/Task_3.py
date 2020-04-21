class Cell:
    def __init__(self, num_cells):
        self.num_cells = int(num_cells)

    def __add__(self, other):
        return self.num_cells + other.num_cells

    def __sub__(self, other):
        if self.num_cells >= other.num_cells:
            return self.num_cells - other.num_cells
        else:
            return print('Разность клеток не может быть отрицательной!')

    def __mul__(self, other):
        return self.num_cells * other.num_cells

    def __truediv__(self, other):
        return self.num_cells // other.num_cells


# todo    def make_order(self, num_cells, num_row):


cells_1 = Cell(4)
cells_2 = Cell(2)

print(cells_1 + cells_2)
print(cells_1 - cells_2)
print(cells_1 * cells_2)
print(cells_1 / cells_2)
