class Worker:

    def __init__(self, name, surname, position, dict_income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict_income


class Position(Worker):

    def get_full_name(self):
        return print((str(self.name) + ' ' + str(self.surname)).title())

    def get_total_income(self):
        return print(f'Зарплата: {self._income["wage"]}\n'
                     f'Премия: {self._income["bonus"]}\n'
                     f'Суммарный доход: {self._income["wage"] + self._income["bonus"]}')


income_dict = {"wage": 13000, "bonus": 20000}

position = Position('Иван', 'Иванов', 'Директор', income_dict)
position.get_full_name()
position.get_total_income()

print(position._income)
