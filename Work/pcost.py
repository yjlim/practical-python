# pcost.py
#
# Exercise 1.27
import os

total = 0

f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
for line in f:
    row = line.split(',')
    total = total + int(row[1])*float(row[2][:-1])

print(f'Total cost {total}')
f.close()
