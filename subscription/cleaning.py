import pandas as pd
import os

# Загрузка данных
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cleaned_subscription_transactions.csv'))
path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cleaned_attributes.csv'))


# Загрузка данных
data1 = pd.read_csv(path1)
data2 = pd.read_csv(path2)

# Приведение колонок в нижний регистр для унификации
data1.columns = data1.columns.str.lower()
data2.columns = data2.columns.str.lower()

# Получение пересечения уникальных customer_account_id из обеих таблиц
common_ids = set(data1['customer_account_id']).intersection(set(data2['customer_account_id']))

# Фильтрация данных по общим customer_account_id
data1_cleaned = data1[data1['customer_account_id'].isin(common_ids)]
data2_cleaned = data2[data2['customer_account_id'].isin(common_ids)]

# Проверка результатов
print(f"Размеры данных после очистки:\n"
      f"cleaned_subscription_transactions: {data1_cleaned.shape}\n"
      f"cleaned_attributes: {data2_cleaned.shape}")

# Сохранение результатов в новые CSV файлы (опционально)
data1_cleaned.to_csv('cleaned_subscription_transactions_f.csv', index=False)
data2_cleaned.to_csv('cleaned_attributes_f.csv', index=False)
