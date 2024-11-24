import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Загрузка данных
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cleaned_subscription_transactions.csv'))
data=pd.read_csv(path1)

# Оставляем только числовые данные
numeric_data = data.select_dtypes(include=["number"])

# Проверяем, какие столбцы остались
print("Числовые столбцы:")
print(numeric_data.columns)

# Рассчитываем корреляционную матрицу
correlation_matrix = numeric_data.corr()

# Выводим корреляционную матрицу
print("\nКорреляционная матрица:")
print(correlation_matrix)

# Визуализация корреляционной матрицы
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Корреляционная матрица")
plt.show()
