import matplotlib.pyplot as plt
import pandas as pd
import os

# Пути к файлам
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'attributes.csv'))
# Загрузка данных
data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Гистограмма для 'amount'
plt.figure(figsize=(8, 6))
data1['amount'].hist(bins=20, color='skyblue', alpha=0.8)
plt.title('Распределение сумм транзакций (amount)')
plt.xlabel('Сумма')
plt.ylabel('Частота')

# Гистограмма для 'age'
plt.figure(figsize=(8, 6))
data2['age'].value_counts().sort_index().plot(kind='bar', color='purple', alpha=0.8)
plt.title('Распределение возрастов')
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.show()


