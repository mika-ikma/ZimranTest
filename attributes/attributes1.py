import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import csv

file_path = './attributes.csv'
data = pd.read_csv(file_path)

rows = 25

with open (file_path, mode = 'r', encoding= 'utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    table = PrettyTable()
    table.field_names = header

    for i, row in enumerate(csv_reader):
        if i >= rows:
            break
        table.add_row(row)

    print(table)