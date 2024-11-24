import pandas as pd
import os

# Загрузка данных
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cleaned_subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cleaned_attributes.csv'))


data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Преобразуем ключевые столбцы в строки, если нужно (чтобы избежать несоответствий типов данных)
data1['customer_account_id'] = data1['customer_account_id'].astype(str)
data2['customer_account_id'] = data2['customer_account_id'].astype(str)

# Найдем ключи, которые есть в data1, но отсутствуют в data2
missing_in_data2 = set(data1['customer_account_id']) - set(data2['customer_account_id'])
missing_in_data2_df = data1[data1['customer_account_id'].isin(missing_in_data2)]

# Найдем ключи, которые есть в data2, но отсутствуют в data1
missing_in_data1 = set(data2['customer_account_id']) - set(data1['customer_account_id'])
missing_in_data1_df = data2[data2['customer_account_id'].isin(missing_in_data1)]

# Выводим результаты
print(f"Количество записей в data1, отсутствующих в data2: {len(missing_in_data2)}")
print(f"Количество записей в data2, отсутствующих в data1: {len(missing_in_data1)}")


# Для проверки можно вывести примеры записей
print("\nПримеры записей, которые есть в data1, но отсутствуют в data2:")
print(missing_in_data2_df.head())

print("\nПримеры записей, которые есть в data2, но отсутствуют в data1:")
print(missing_in_data1_df.head())
