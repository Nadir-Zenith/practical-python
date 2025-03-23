# pcost.py
#
# Exercise 1.27

path = "./Data/portfolio.csv"
total_cost = 0
with open(path, 'r') as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        total_cost += int(row[1]) * float(row[2])

print(f'{total_cost=}')
