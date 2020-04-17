import argparse


def salary(working_time, cost_per_hour, bonus):
    return (working_time * cost_per_hour) + bonus


parse = argparse.ArgumentParser()

parse.add_argument('time', type=int, help='Working time')
parse.add_argument('cost', type=int, help='Cost per hour')
parse.add_argument('bonus', type=int, help='Bonus for work')

args = parse.parse_args()

print(f'Заработная плата составит: {salary(args.time, args.cost, args.bonus)}')
