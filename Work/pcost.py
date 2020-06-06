# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename: str):
    with open(f'{filename}', 'rt') as f:
        total = 0
        rows = csv.reader(f)
        headers = next(rows)
        for fields in rows:
            #fields = line.split(',')
            try:
                shares = int(fields[1])
                cost = float(fields[2])
            except ValueError:
                print("Couldn't parse", line)
            total = total + shares*cost
        return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)
