import pandas as pd
import matplotlib.pyplot as plt

file_path = 'subscription_transactions.csv'
data = pd.read_csv(file_path)


# Преобразовываем в хронологию
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

duplicates = data[data.duplicated(subset=['customer_account_id', 'payment_type'], keep=False)]
print(duplicates[duplicates['payment_type'] == 'first'])


first_transactions = data[data['payment_type'] == 'first']
unique_first_transactions = first_transactions['customer_account_id'].nunique()
total_first_transactions = len(first_transactions)
print(f"Уникальные пользователи: {unique_first_transactions}")
print(f"Всего транзакций: {total_first_transactions}")

print(data)

