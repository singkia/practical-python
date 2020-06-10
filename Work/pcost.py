# pcost.py
#
# Exercise 1.27


total_cost = 0.0

with open('C:/Users/LO/Documents/GitHub/practical-python/Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price

    print('Total cost', total_cost)





'''
import os

total_cost = 0
s_cost = 0

with open('C:/Users/LO/Documents/GitHub/practical-python/Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        s_cost = float(row[1]) * float(row[2])
        total_cost += s_cost
        s_cost = 0

    print('Total cost', total_cost)

    
'''
