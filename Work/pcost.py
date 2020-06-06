# pcost.py
#
# Exercise 1.27
import os

def portfolio_cost(filename: str):
    with open(f'{filename}', 'rt') as f:
        total = 0
        headers = next(f).split(',')
        for line in f:
            fields = line.split(',')
            try:
                shares = int(fields[1])
                cost = float(fields[2][:-1])
            except ValueError:
                print("Couldn't parse", line)
            total = total + shares*cost

        print(f'Total cost {total}')
