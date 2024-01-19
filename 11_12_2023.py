import pandas as pd
import numpy as np

#series

# my_series = pd.Series([1, 2, 3, 4, 5])
# print(my_series)

# s = pd.Series(np.random.randn(5), index=['a', 'b', '5', 't', 'e'])
# print(s)


# Dataframe
# df = pd.DataFrame(np.random.randn(8, 3),index=pd.date_range('1/1/2000', periods=8), columns=['A', 'B', 'C'])
# print(df)

#Загрузка и сохранение данных

# #csv
# data = pd.read_csv('C:/Users/user/Desktop/Python_cource/cereal.csv', sep=';', decimal=',')
# data.to_csv('cereal.xlsx')
#
# #xmls
# data_2 = pd.read_xmls('C:/Users/user/Desktop/Python_cource/cereal.xlsx', sheetname='1')
# data_2.to_csv('cereal.csv')
# print(data)
#
# #HDF5
# pd.read_hdf('cereal.h5', 'df')
# df.to_hdf('cereal.h5', 'df')


# df = pd.DataFrame({
#     'country':["Russia", "Belarus", "Kazahstan"],
#     'population': [17.04, 20.07, 45.5 ],
#     'squre': [27224904, 17125191, 603628]}, index=['1', '2', '3'])
# df = df.rename(columns={'country': 'Страна', 'population': 'Население', 'squre': 'Площадь'})
#
#
# df.to_csv('contries.csv', sep=';', decimal=',')
# df = pd.read_csv('contries.csv', sep=',')

# .groupby.

titanic_df = pd.read_csv('titanic.csv')
print(titanic_df.groupby(('Sex'))['Age'].mean(numeric_only=True))
# print(titanic_df.head(2))

# Загрузите файл.
# Выведите первые 5 строк.
# Выведите средние арифметические, минимумы и максимумы по всем колонкам.
#
# cereal_data = pd.read_csv('cereal.csv', sep=';', decimal=',')
# print(cereal_data.head(5))

# # Расчет среднего, минимума и максимума
# mean_values = cereal_data.mean(numeric_only=True)
# min_values = cereal_data.min(numeric_only=True)
# max_values = cereal_data.max(numeric_only=True)
#
# # Вывод результатов
# print("Средние значения:")
# print(mean_values)
# print("\nМинимальные значения:")
# print(min_values)
# print("\nМаксимальные значения:")
# print(max_values)






