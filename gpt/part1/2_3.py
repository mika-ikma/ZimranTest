import pandas as pd
import os
from prettytable import PrettyTable

# Пути к файлам
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'attributes.csv'))

# Загрузка данных
data = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Устанавливаем формат отображения
pd.options.display.float_format = '{:.2f}'.format
import pandas as pd
from prettytable import PrettyTable

def describe_combinations_to_prettytable(data, group_columns, target_column):
    """Функция для вычисления статистики по всем возможным комбинациям категориальных параметров"""
    grouped = data.groupby(group_columns)[target_column].describe()
    
    # Создаем таблицу PrettyTable
    table = PrettyTable()
    table.field_names = ["Комбинация"] + list(grouped.columns)
    
    # Заполняем таблицу
    for index, stats in grouped.iterrows():
        combination = ", ".join([f"{col}: {val}" for col, val in zip(group_columns, index)])
        table.add_row([combination] + list(stats))
    
    print(f"\nСтатистика для {target_column}, сгруппированная по комбинациям: {group_columns}")
    print(table)



# Вычисляем статистику для всех комбинаций категорий
describe_combinations_to_prettytable(data, ['payment_type', 'currency', 'offer'], 'amount')
