import pandas as pd
import matplotlib.pyplot as plt

file_path = './subscription_transactions.csv'
data = pd.read_csv(file_path)


# Преобразовываем в хронологию
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# 
transaction_by_payment_type = data.groupby('payment_type').size()
unique_customer_by_payement_type = data.groupby('payment_type')['customer_account_id'].nunique()
average_transaction_by_user = transaction_by_payment_type/unique_customer_by_payement_type

print("Среднее кол-во транзакций на пользователя по типам оплаты")
print(average_transaction_by_user)
