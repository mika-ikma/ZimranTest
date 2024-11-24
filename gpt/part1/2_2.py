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

import pandas as pd
from prettytable import PrettyTable

def describe_to_prettytable(data, group_column, target_column, table_name):
    """Функция для отображения статистики числовой колонки по категориям"""
    grouped = data.groupby(group_column)[target_column].describe()
    
    # Создаем таблицу PrettyTable
    table = PrettyTable()
    table.field_names = ["Категория"] + list(grouped.columns)
    
    # Заполняем таблицу данными
    for category, stats in grouped.iterrows():
        table.add_row([category] + list(stats))
    
    print(f"\nСтатистика для {target_column}, сгруппированная по '{group_column}' ({table_name}):")
    print(table)



# 1. Статистика по 'payment_type'
describe_to_prettytable(data1, 'payment_type', 'amount', 'Статистика по payment_type')

# 2. Статистика по 'currency'
describe_to_prettytable(data1, 'currency', 'amount', 'Статистика по currency')

# 3. Статистика по 'offer'
describe_to_prettytable(data1, 'offer', 'amount', 'Статистика по offer')
