import pandas as pd
# 1.
# m = [2, 3 ,4]
# print([(i, i**2) for i in m])

# 2.Выберите из предложенных наборов данных наиболее интересный для вас, и выполните исследовательский анализ данных, следуя шагам, описанным в лекции.


# data = pd.read_csv('2.2 cereal.csv', sep=',', decimal='.')  # Укажите путь к вашему файлу и символ разделителя
#
# # Вывод первых 5 строк и последних 5 строк таблицы на экран
# print(data.head(5))
# print(data.tail(5))
#
# # Просмотр типов данных в таблице и краткое описание данных
# print(data.info())
# print(data.describe())
#
# #Пропущенные значения: Некоторые столбцы содержат пропущенные значения, например, в столбце "potass".
# #Пропущенные значения в столбце "potass" можно заполнить, например, средним значением или медианой этого столбца.
# data['potass'].fillna(mean_potass, inplace=True)

# 3.

# file_path = 'C:\\2.3 clients_countries_.csv'
# df = pd.read_csv('clients_contries.csv', sep = ',', decimal='.')
# counts = df.groupby('countries')['client_id'].count()
# avg_ages = df.groupby('countries')['age'].mean()
# print(counts)
# print(avg_ages)

#4
# sales_path  = pd.read('sales.csv.csv', sep = ',', decimal='.')
# weather_path = pd.read ('weather.csv.csv', sep = ',', decimal='.')
# sales_df = pd.read_csv('sales.csv', index_col='date', usecols=['date', 'date'])
# weather_df = pd.read_csv('weather.csv', index_col='date', usecols=['date', 'temperature'])
# result = weather_df.join(sales_df)
# print(result)



#5
# import pandas as pd
# from matplotlib import pyplot as plt

df = pd.read_csv('AI_lectures/2.5 donut.csv')

plt.hist2d(df['x'], df['y'], bins=100)
