class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_num(cls, date):
        date_num = [int(el) for el in str(date).split('-')]
        return print(date_num)

    @staticmethod
    def validator(date):
        date_list = [int(el) for el in str(date).split('-')]
        if date_list[0] > 31:
            print('Неверный формат дней!')
        else:
            if date_list[1] > 12 or date_list[1] < 1:
                print('Неверный формат месяца!')
            else:
                if date_list[2] < 1960 or date_list[2] > 2200:
                    print('Неверный формат года!')
                else:
                    print(date_list)


Date.date_num('25-02-1988')
Date.validator('5-10-1938')
