import pandas as pd
import matplotlib.pyplot as plt
import os

# Загружаем данные
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_attributes.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_subscription_transactions.csv'))

# Загрузка данных
transactions = pd.read_csv(path1)
attributes = pd.read_csv(path2)

# Объединение таблиц по customer_account_id
merged_data = pd.merge(transactions, attributes, on='customer_account_id', how='inner')

# Проверка объединённых данных
print("Размер объединённой таблицы:", merged_data.shape)
print(merged_data.head())

# Сохранение объединённой таблицы (опционально)
# merged_data.to_csv('merged_data.csv', index=False)
# Группировка по ltv_source
source_analysis = merged_data.groupby('ltv_source').agg(
    total_revenue=('amount', 'sum'),
    total_clients=('customer_account_id', 'nunique')
).sort_values(by='total_revenue', ascending=False).reset_index()

# Визуализация
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.barh(source_analysis['ltv_source'], source_analysis['total_revenue'], color='skyblue')
plt.title('Наиболее эффективные источники привлечения')
plt.xlabel('Общая выручка')
plt.ylabel('Источник')
plt.grid()
plt.show()

