revenue = int(input('Введите значение выручки за период: '))
costs = int(input('Введите значение издержек за период: '))
profit = revenue - costs

if revenue > costs:
    profitability = profit / revenue
    print(f'Финансовый результат: прибыль в размере {profit}')
    print(f'Рентабельность выручки составляет: {profitability:.2f}')
    employees = int(input('Укажите численность сотрудников: '))
    profit_emp = profit / employees
    print(f'Прибыль на одного сотрудника составляет: {profit_emp}')
else:
    print(f'Финансовый результат: убыток в размере {profit}')