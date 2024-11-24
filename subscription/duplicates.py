import pandas as pd
import os

# Загрузка данных
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'subscription_transactions.csv'))
data = pd.read_csv(path1)

# Преобразуем колонку subscription_cohort_date в datetime для удобства
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# Поиск дубликатов по 'customer_account_id' и 'subscription_cohort_date'
duplicates = data[data.duplicated(subset=['customer_account_id', 'subscription_cohort_date', 'offer', 'payment_type', 'amount'], keep=False)]

# Вывод количества дубликатов и их просмотр
print(f"Найдено {duplicates.shape[0]} строк с дубликатами.")
#print(duplicates)

# Сохранение для анализа, если нужно
duplicates.to_csv('duplicates_analysis(subscription).csv', index=False)

# Рекомендуем использовать PrettyTable для удобного отображения, если объем данных небольшой
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = duplicates.columns.tolist()

for _, row in duplicates.iterrows():
    table.add_row(row.tolist())

#print(table)
