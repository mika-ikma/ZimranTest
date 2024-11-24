import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загружаем данные
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_attributes.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_subscription_transactions.csv'))

# Загрузка данных
transactions = pd.read_csv(path1)
attributes = pd.read_csv(path2)



# Объединение таблиц
merged_data = pd.merge(transactions, attributes, on='customer_account_id', how='inner')

# Переименование колонок для ясности
merged_data.rename(columns={
    'payment_type_x': 'subscription_payment_type',  # Тип оплаты из transactions
    'payment_type_y': 'attributes_payment_type'     # Тип оплаты из attributes
}, inplace=True)

# Проверяем новые названия колонок
print("Объединённые данные с переименованными колонками:")
print(merged_data.head())

# Преобразование категориальных переменных в числовые
merged_data['subscription_payment_type_encoded'] = merged_data['subscription_payment_type'].astype('category').cat.codes
merged_data['attributes_payment_type_encoded'] = merged_data['attributes_payment_type'].astype('category').cat.codes
merged_data['offer_encoded'] = merged_data['offer'].astype('category').cat.codes
merged_data['ltv_source_encoded'] = merged_data['ltv_source'].astype('category').cat.codes

# Корреляционная матрица
correlation_data = merged_data[['subscription_payment_type_encoded', 'attributes_payment_type_encoded', 'offer_encoded', 'ltv_source_encoded', 'amount']]
correlation_matrix = correlation_data.corr()

# Визуализация корреляционной матрицы с улучшением читаемости
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 12})
plt.title('Корреляции между источниками, типами оплат и предложениями', fontsize=16, pad=20)
plt.xticks(fontsize=12, rotation=45, ha='right')
plt.yticks(fontsize=12, rotation=0)
plt.tight_layout()
plt.show()