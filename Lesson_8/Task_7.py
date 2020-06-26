class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


number_1 = complex(3, 2)
number_2 = complex(4, 5)

complex_num_1 = ComplexNumber(number_1)
complex_num_2 = ComplexNumber(number_2)

print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2)
