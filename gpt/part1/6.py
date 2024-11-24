import matplotlib.pyplot as plt
import pandas as pd
import os

# Пути к файлам
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'attributes.csv'))
# Загрузка данных
data2 = pd.read_csv(path2)

# Популярность источников
plt.figure(figsize=(12, 10))
data2['saving_money_for'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (saving_money_for)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()
# Популярность источников
plt.figure(figsize=(12, 10))
data2['time_for_target'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (time_for_target)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()
# Популярность источников
plt.figure(figsize=(12, 10))
data2['language_group'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (language_group)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()

# Популярность типов оплаты
plt.figure(figsize=(12, 10))
data2['payment_type'].value_counts().plot(kind='bar', color='green', alpha=0.8)
plt.title('Популярность типов оплаты (payment_type)')
plt.xlabel('Тип оплаты')
plt.ylabel('Количество')
plt.show()

# Популярность источников
plt.figure(figsize=(12, 10))
data2['device_type'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (device_type)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()
# Популярность источников
plt.figure(figsize=(12, 10))
data2['geo'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (geo)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()
# Популярность источников
plt.figure(figsize=(12, 10))
data2['gender'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (gender)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()

# Популярность источников
plt.figure(figsize=(12, 10))
data2['ltv_source'].value_counts().plot(kind='bar', color='orange', alpha=0.8)
plt.title('Популярность источников (ltv_source)')
plt.xlabel('Источник')
plt.ylabel('Количество')
plt.show()
