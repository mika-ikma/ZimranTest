import pandas as pd
import matplotlib.pyplot as plt
import os

# Загружаем данные
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_subscription_transactions.csv'))
data = pd.read_csv(path)

# Преобразуем дату в формат datetime
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# Группировка по месяцам
grouped_data = data.groupby(data['subscription_cohort_date'].dt.to_period('M')).agg(
    total_transactions=('customer_account_id', 'count'),
    unique_clients=('customer_account_id', 'nunique')
).reset_index()

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(grouped_data['subscription_cohort_date'].astype(str), grouped_data['total_transactions'], label='Total Transactions')
plt.plot(grouped_data['subscription_cohort_date'].astype(str), grouped_data['unique_clients'], label='Unique Clients')
plt.title('Динамика транзакций и уникальных клиентов')
plt.xlabel('Месяц')
plt.ylabel('Количество')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()
