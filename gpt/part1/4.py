import pandas as pd
import os
from prettytable import PrettyTable

# Функция для создания PrettyTable
def display_table(title, column_names, rows):
    table = PrettyTable()
    table.title = title
    table.field_names = column_names
    for row in rows:
        table.add_row(row)
    print(table)

# Пути к файлам
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))

# Загрузка данных
data = pd.read_csv(path)

# Пропущенные значения
missing_rows = [[col, missing] for col, missing in data.isnull().sum().items()]
display_table("Пропущенные значения", ["Столбец", "Пропущенные значения"], missing_rows)