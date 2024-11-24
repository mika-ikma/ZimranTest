import pandas as pd
import os

# Загрузка данных
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'attributes.csv'))
data = pd.read_csv(path1)

# Преобразуем колонку date в datetime для удобства
data['date'] = pd.to_datetime(data['date'])

# Удаление дубликатов, оставляя только первую строку для каждого набора дубликатов
cleaned_data = data.drop_duplicates(subset=['customer_account_id', 'date'], keep='first')

# Сохранение очищенных данных в новый CSV-файл
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'cleaned_attributes.csv'))
cleaned_data.to_csv(output_path, index=False)

print(f"Данные успешно очищены. Новый файл сохранен по пути: {output_path}")

# Для проверки
print(f"Размер очищенных данных: {cleaned_data.shape}")
