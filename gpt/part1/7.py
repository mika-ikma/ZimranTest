import matplotlib.pyplot as plt
import pandas as pd
import os

# Пути к файлам
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'attributes.csv'))
# Загрузка данных
data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Конвертация даты в datetime
data1['subscription_cohort_date'] = pd.to_datetime(data1['subscription_cohort_date'])

# Группировка по дням
subscription_by_date = data1.groupby('subscription_cohort_date').size()

# Построение графика
plt.figure(figsize=(10, 6))
subscription_by_date.plot(kind='line', color='blue', alpha=0.8)
plt.title('Динамика транзакций по времени')
plt.xlabel('Дата')
plt.ylabel('Количество транзакций')
plt.show()

# 
#
#Конвертация даты в datetime 
data2['date'] = pd.to_datetime(data2['date'])

# Группировка по дням
transactions_by_date = data2.groupby('date').size()

# Построение графика
plt.figure(figsize=(10, 6))
transactions_by_date.plot(kind='line', color='blue', alpha=0.8)
plt.title('Динамика транзакций по времени')
plt.xlabel('Дата')
plt.ylabel('Количество транзакций')
plt.show()