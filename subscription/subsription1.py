import pandas as pd
import matplotlib.pyplot as plt

file_path = './subscription_transactions.csv'
data = pd.read_csv(file_path)

#print(data.head())

# Преобразовываем в хронологию
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# Кол-во покупок 
transcations_by_date = data.groupby('subscription_cohort_date').size()

# Построение графика 
plt.figure(figsize=(10, 6))
transcations_by_date.plot(kind = 'bar', color='blue', alpha=0.8)
plt.title('Кол-во транзакций по времени')
plt.xlabel('Время')
plt.ylabel('Транзакции')
plt.xticks(ticks=range(0, len(transcations_by_date), 10), rotation = 90)
plt.tight_layout()


# Распределение сумм
plt.figure(figsize=(10, 6))
data['amount'].hist(bins=20, color='green', alpha=0.7)
plt.title('Распеределение Сумм')
plt.xlabel('Сумма')
plt.ylabel('Частота')
plt.tight_layout()


# Анализ по типу оплаты 
payment_types = data['payment_type'].value_counts()

plt.figure(figsize=(10, 6))
payment_types.plot(kind='bar', color='orange', alpha=0.8)
plt.title('Распределение по типу оплаты')
plt.xlabel('Тип оплаты')
plt.ylabel('Кол-во транзакций')
plt.tight_layout()


# Анализ по типу оплаты 
offers = data['offer'].value_counts()

plt.figure(figsize=(10, 6))
offers.plot(kind='bar', color='purple', alpha=0.8)
plt.title('Популярность предложений')
plt.xlabel('Предложение (offer)')
plt.ylabel('Кол-во транзакций')
plt.tight_layout()
plt.show()