import csv
from prettytable import PrettyTable

path = './subscription_transactions.csv'

rows = 25

with open (path, mode = 'r', encoding= 'utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    table = PrettyTable()
    table.field_names = header

    for i, row in enumerate(csv_reader):
        if i >= rows:
            break
        table.add_row(row)

    print(table)