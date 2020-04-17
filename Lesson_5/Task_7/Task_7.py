import json

from Task_3.Task_3 import mean
from Task_6.Task_6 import modified_list

firm_list = [string.strip() for string in open('Firms.txt', encoding='utf-8')]
firm_list = [el.split(' ') for el in firm_list]

profit_list = []
dict_firms_profit = {}
dict_firms_loss = {}
result_list = []
for el in modified_list(firm_list):
    profit = int(el[2]) - int(el[3])
    if profit > 0:
        profit_list.append(profit)
        dict_firms_profit.update({el[0]: profit})
    elif profit < 0:
        dict_firms_loss.update({el[0]: profit})

result_list.append(dict_firms_profit)
result_list.append(dict_firms_loss)
result_list.append({'average_profit': mean(profit_list)})

with open('Task_7.json', 'w') as file:
    json.dump(result_list, file)
