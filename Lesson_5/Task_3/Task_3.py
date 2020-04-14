def mean(some_list):
    return sum(some_list) / len(some_list)


if __name__ == '__main__':
    lines = [line.strip() for line in open('List_of_employees.txt', encoding='utf-8')]

    list_salary = [float(el.split()[1]) for el in lines]
    list_min_salary = [el.split()[0] for el in lines if float(el.split()[1]) < 20000]

    print(f'Employees with a salary less than 20,000: {", ".join(list_min_salary)}')
    print(f'Mean salary: {mean(list_salary):.2f}')
