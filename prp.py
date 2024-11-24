import pandas as pd
import os

# Загрузка данных
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cleaned_subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cleaned_attributes.csv'))


data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Уникальные пользователи
unique_users = data1['customer_account_id'].nunique()

# Общее количество транзакций
total_transactions = len(data1)

# Среднее количество транзакций на пользователя
average_transactions_per_user = total_transactions / unique_users

print(f"Уникальных пользователей: {unique_users}")
print(f"Общее количество транзакций: {total_transactions}")
print(f"Среднее количество транзакций на пользователя: {average_transactions_per_user:.2f}")
print(len(data2))