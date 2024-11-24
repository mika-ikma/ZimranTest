import pandas as pd
import matplotlib.pyplot as plt

file_path = './subscription_transactions.csv'
data = pd.read_csv(file_path)


# Преобразовываем в хронологию
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# Уникальные id по типам оплаты
unique_customer_by_payement_type = data.groupby('payment_type')['customer_account_id'].nunique()
print("Кол-во уникальных аккаунтов по типу оплаты")
print(unique_customer_by_payement_type)

plt.figure(figsize=(10, 6))
unique_customer_by_payement_type.plot(kind='bar', color='purple', alpha=0.8)
plt.title('Динамика пользователей по типу оплаты')
plt.xlabel('Тип оплаты')
plt.ylabel('Кол-во уникальных пользователей')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()