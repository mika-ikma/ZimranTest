import pandas as pd
import matplotlib.pyplot as plt


file_path = './attributes.csv'
data = pd.read_csv(file_path)

data['date'] = pd.to_datetime(data['date'])

# 1. Подсчет общего количества клиентов
total_customers = len(data['customer_account_id'])
print(f"Общее количество записей клиентов: {total_customers}")

# 2. Подсчет количества уникальных клиентов
unique_customers = data['customer_account_id'].nunique()
print(f"Количество уникальных клиентов: {unique_customers}")

# 3. Подсчет общего количества записей в данных
total_records = len(data)
print(f"Общее количество записей в данных: {total_records}")

# 4. Проверка наличия пустых (null) значений
null_counts = data.isnull().sum()
total_nulls = null_counts.sum()
print("\nКоличество пустых значений по колонкам:")
print(null_counts)

if total_nulls > 0:
    print(f"\nВсего пустых значений в данных: {total_nulls}")
else:
    print("\nВ данных нет пустых значений!")
