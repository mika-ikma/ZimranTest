import pandas as pd

# Загрузка данных
data = pd.read_csv('cleaned_subscription_transactions.csv')

# Добавление колонки с индексами (начиная с 1)
data['Row Index'] = range(1, len(data) + 1)

# Сохранение данных
data.to_csv('subscription_transactions_index.csv', index=False)
