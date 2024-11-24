import pandas as pd
import matplotlib.pyplot as plt


file_path = './attributes.csv'
data = pd.read_csv(file_path)

data['date'] = pd.to_datetime(data['date'])

a = data.groupby('ltv_source').size()

b = data.groupby('ltv_source')['customer_account_id'].nunique()

#
x= range(len(a)) #
width = 0.4 #

#
plt.figure(figsize=(10, 6))

#
plt.bar([pos - width / 2 for pos in x], a, width = width, color='purple', alpha = 0.8, label = 'Кол-во записей')
#
plt.bar([pos + width / 2 for pos in x], b, width = width, color='orange', alpha = 0.8, label = 'Кол-во уникальных клиентов')


# Настройка графика
plt.title('Сравнение общего числа записей и уникальных клиентов')
plt.xlabel('Способ знакомства')
plt.ylabel('Кол-во')
plt.xticks(x, a.index, rotation=90)  # Устанавливаем метки x оси
plt.legend()
plt.tight_layout()

plt.show()