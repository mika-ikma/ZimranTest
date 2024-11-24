import pandas as pd
import os
from prettytable import PrettyTable

# Пути к файлам
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'attributes.csv'))

# Загрузка данных
data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Устанавливаем формат отображения
pd.options.display.float_format = '{:.2f}'.format

def describe_to_prettytable(data, table_name):
    """Функция для преобразования describe() в таблицу PrettyTable"""
    description = data.describe()
    table = PrettyTable()
    
    # Добавляем заголовки
    table.field_names = ["Статистика"] + list(description.columns)
    
    # Добавляем строки с данными
    for index, row in description.iterrows():
        table.add_row([index] + list(row))
    
    print(f"\nСтатистика числовых колонок: {table_name}")
    print(table)

# Статистика для числовых данных
describe_to_prettytable(data1, "subscription_transactions.csv")
describe_to_prettytable(data2, "attributes.csv")
