import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
x = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader
 print(row)

