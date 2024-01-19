import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
import random
import math

POINTS = 100000

data = {
    'normal': np.random.randn(POINTS),
    'uniform': [random.random() for _ in range(POINTS)],
    'x': np.linspace(0, 10, POINTS),
}

data['sin'] = [math.sin(x) for x in data['x']]
data['noisy'] = [x + random.random() for x in data['x']]
data['noisy2'] = [x + np.random.randn() for x in data['x']]


df = pd.DataFrame(data)

df['noisy_sin'] = df['sin'] + df['noisy2']

print(data)

# Построение графика:
# df.plot(x='x', y='sin')

#Построение гистограммы:
# df['normal'].hist(bins=50)
#
#Диаграмма рассеивания
# plt.scatter(df['x'], df['noisy_sin'], marker='.')

# Задание
# # Постройте графики и гистограммы для каждого столбца предложенного набора данных (который генерируется кодом).
# # + Постройте двумерную гистограмму для предложенного набора данных (donut.csv).

#





