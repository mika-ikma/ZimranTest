import pandas as pd
import os
from prettytable import PrettyTable

# Загрузка данных
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'susbscription.csv'))
data = pd.read_csv(file_path)

# Убедимся, что столбец `customer_account_id` существует в данных
if 'customer_account_id' not in data.columns:
    raise ValueError("В файле отсутствует столбец 'customer_account_id'.")

# Преобразуем столбец `date` в формат datetime
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Используем `errors='coerce'` для обработки ошибок

# Группировка по клиентам и подсчет повторений
repeated_customers = data.groupby('customer_account_id').size()

# Подсчет общего количества клиентов
total_customers = data('susbscription_cohort_date')['customer_account_id'].nunique()
print(f"Общее количество уникальных клиентов: {total_customers}")

# Оставляем только повторяющихся клиентов
repeated_customers = repeated_customers[repeated_customers > 1]

# PrettyTable для повторяющихся клиентов
if not repeated_customers.empty:
    repeated_table = PrettyTable()
    repeated_table.field_names = ["Customer Account ID", "Количество повторений"]

    for customer_id, count in repeated_customers.items():
        repeated_table.add_row([customer_id, count])

    print("\nПовторяющиеся клиенты:")
    print(repeated_table)

# Вывод количества повторяющихся клиентов
print(f"\nКоличество повторяющихся клиентов: {len(repeated_customers)}")

# Пример: Показать данные для одного клиента
if not repeated_customers.empty:
    specific_customer_id = repeated_customers.index[0]  # Берем ID первого повторяющегося клиента
    customer_data = data[data['customer_account_id'] == specific_customer_id]

    # PrettyTable для данных по конкретному клиенту
    customer_table = PrettyTable()
    customer_table.field_names = customer_data.columns.tolist()

    for _, row in customer_data.iterrows():
        customer_table.add_row(row.tolist())

    print(f"\nДанные для клиента {specific_customer_id}:")
    print(customer_table)
else:
    print("Повторяющихся клиентов не найдено.")
