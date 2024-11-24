import pandas as pd
from prettytable import PrettyTable
import os

# Загрузка данных
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cleaned_subscription_transactions.csv'))
data = pd.read_csv(path1)


# Преобразуем дату
data['subscription_cohort_date'] = pd.to_datetime(data['subscription_cohort_date'])

# Добавляем месяц подписки (используем как transaction_month, так как другой даты нет)
data['cohort_month'] = data['subscription_cohort_date'].dt.to_period('M')
data['transaction_month'] = data['subscription_cohort_date'].dt.to_period('M')  # Фиктивная транзакционная дата

# Определяем разницу в месяцах между транзакцией и датой подписки
data['months_difference'] = (data['transaction_month'] - data['cohort_month']).apply(lambda x: x.n)

# Создаем когортную таблицу
cohort_table = data.pivot_table(
    index='cohort_month',
    columns='months_difference',
    values='customer_account_id',
    aggfunc='nunique'
).fillna(0).astype(int)

# Определяем количество месяцев
num_months = cohort_table.shape[1]

# Генерация таблицы для PrettyTable
table = PrettyTable()
table.field_names = ['Cohort Month'] + [f'Month {i}' for i in range(num_months)]
for index, row in cohort_table.iterrows():
    table.add_row([str(index)] + list(row))

# Вывод таблицы
print(table)