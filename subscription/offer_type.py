import pandas as pd
import matplotlib.pyplot as plt

file_path = './subscription_transactions.csv'
data = pd.read_csv(file_path)


# Преобразовываем в хронологию
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# Кол-во покупок 
transcations_by_offers = data.groupby(['subscription_cohort_date', 'offer']).size().unstack(fill_value=0)


# Построение графика 
offers = transcations_by_offers.columns

for offer in offers:
    plt.figure(figsize=(10, 6))
    transcations_by_offers[offer].plot(kind='line', color='blue', alpha=0.8)
    plt.title(f'Динамика транзакций: {offer}')
    plt.xlabel('Дата')
    plt.ylabel('Кол-во транзакций')
    plt.grid(True)
    plt.tight_layout()
plt.show()
        