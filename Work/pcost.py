# pcost.py
#
# Exercise 1.27

total_cost = 0
with open('Data/portfolio.csv', 'rt') as f:
    header = next(f)
    for line in f:
        stock_data = line.split(',')
        total_cost = total_cost + int(stock_data[1]) * float(stock_data[2])

print('Total cost ', str(total_cost))