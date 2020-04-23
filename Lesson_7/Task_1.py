class Matrix:
    def __init__(self, *args):
        self.matrix_list = list(args)

    def __str__(self):
        self.str = '\n'.join(['\t'.join([str(el) for el in row]) for row in self.matrix_list])
        return self.str

    def __add__(self, other):
        matrix_sum = [list(zip(self.matrix_list[i], other.matrix_list[i])) for i in range(len(self.matrix_list))]
        result = [list(map(sum, tup)) for tup in matrix_sum]
        return Matrix(result)


list1 = [1, 2, 3]
list2 = [1, 1, 1]
list3 = [3, 2, 1]

matrix1 = Matrix(list1, list2, list3)
matrix2 = Matrix(list3, list2, list1)

print(matrix1)
print()
print(matrix2)
print()
print(matrix1 + matrix2)
