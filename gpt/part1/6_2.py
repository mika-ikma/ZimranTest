import matplotlib.pyplot as plt
import pandas as pd
import os

# Пути к файлам
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))

# Загрузка данных
data = pd.read_csv(path)


# Популярность источников
plt.figure(figsize=(12, 10))
data['currency'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (currency)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()

# Популярность типов оплаты
plt.figure(figsize=(12, 10))
data['payment_type'].value_counts().plot(kind='bar', color='green', alpha=0.8)
plt.title('Популярность типов оплаты (payment_type)')
plt.xlabel('Тип оплаты')
plt.ylabel('Количество')
plt.show()

# Популярность источников
plt.figure(figsize=(12, 10))
data['offer'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (offer)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()