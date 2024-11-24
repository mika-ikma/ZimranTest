import pandas as pd
import matplotlib.pyplot as plt

file_path = './subscription_transactions.csv'
data = pd.read_csv(file_path)


# Преобразовываем в хронологию
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# Кол-во покупок 
transcations_by_payment_type = data.groupby(['subscription_cohort_date', 'payment_type']).size().unstack(fill_value=0)
transcations_by_payment_type_smoothed=transcations_by_payment_type.rolling(window=7).mean()

transcations_by_payment_type_smoothed.plot(kind='line', figsize=(12, 6), alpha=0.8)
#transcations_by_payment_type.plot(kind='line', figsize=(12, 6), alpha=0.8)
plt.title(f'Динамика транзакций')
plt.xlabel('Дата')
plt.ylabel('Кол-во транзакций')
plt.grid(True)
plt.tight_layout()
plt.show()