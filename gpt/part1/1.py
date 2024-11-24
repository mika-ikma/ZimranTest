import pandas as pd
import os
from prettytable import PrettyTable

# Пути к файлам
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'attributes.csv'))

# Загрузка данных
data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Функция для создания PrettyTable
def display_table(title, column_names, rows):
    table = PrettyTable()
    table.title = title
    table.field_names = column_names
    for row in rows:
        table.add_row(row)
    print(table)

# Обработка данных1
print("\n=== Анализ данных 1 ===")
# Размер данных
display_table("Размер данных", ["Метрика", "Значение"], [["Количество строк", data1.shape[0]], ["Количество столбцов", data1.shape[1]]])

# Типы данных
dtypes_rows = [[col, dtype] for col, dtype in zip(data1.columns, data1.dtypes)]
display_table("Типы данных (Data 1)", ["Столбец", "Тип данных"], dtypes_rows)

# Пропущенные значения
missing_rows = [[col, missing] for col, missing in data1.isnull().sum().items()]
display_table("Пропущенные значения (Data 1)", ["Столбец", "Пропущенные значения"], missing_rows)

# Первые строки данных
head_rows = data1.head().values.tolist()
display_table("Первые строки данных (Data 1)", data1.columns.tolist(), head_rows)

# Обработка данных2
print("\n=== Анализ данных 2 ===")
# Размер данных
display_table("Размер данных", ["Метрика", "Значение"], [["Количество строк", data2.shape[0]], ["Количество столбцов", data2.shape[1]]])

# Типы данных
dtypes_rows = [[col, dtype] for col, dtype in zip(data2.columns, data2.dtypes)]
display_table("Типы данных (Data 2)", ["Столбец", "Тип данных"], dtypes_rows)

# Пропущенные значения
missing_rows = [[col, missing] for col, missing in data2.isnull().sum().items()]
display_table("Пропущенные значения (Data 2)", ["Столбец", "Пропущенные значения"], missing_rows)

# Первые строки данных
head_rows = data2.head().values.tolist()
display_table("Первые строки данных (Data 2)", data2.columns.tolist(), head_rows)
