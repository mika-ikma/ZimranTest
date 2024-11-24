import pandas as pd
import os
from prettytable import PrettyTable

# Пути к файлам
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'attributes.csv'))

# Загрузка данных
data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

def value_counts_to_prettytable(data, column_name, table_name):
    """Функция для преобразования value_counts() в таблицу PrettyTable"""
    value_counts = data[column_name].value_counts()
    table = PrettyTable()
    table.field_names = ["Значение", "Частота"]
    
    for value, count in value_counts.items():
        table.add_row([value, count])
    
    print(f"\nРаспределение '{column_name}' ({table_name}):")
    print(table)

# Распределение категориальных переменных для data1
print('For subscription_transactions.csv')
value_counts_to_prettytable(data1, 'currency', 'subscription_transactions.csv')
value_counts_to_prettytable(data1, 'offer', 'subscription_transactions.csv')

# Распределение категориальных переменных для data2
print('For attributes.csv')
value_counts_to_prettytable(data2, 'ltv_source', 'attributes.csv')
value_counts_to_prettytable(data2, 'payment_type', 'attributes.csv')
value_counts_to_prettytable(data2, 'device_type', 'attributes.csv')
