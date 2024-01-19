#Seriesn
import numpy as np
import pandas as pd
from pandas import RangeIndex, Index

# my_series = pd.Series([5, 6, 7, 8, 9, 10])
# print(my_series)

# s = pd.Series(np.random.randn(5))
# index = ['a', 'b', 'c', 'd', 'e']
# # print(s)
#
# print (s[1])
#
# print(s.get('z', 'error'))

# my_series.index
# RangeIndex(start=0, stop=6, step=1)
# print(my_series.index)

# my_series2 = pd.Series([5, 6, 7, 8], index=['a', 'b', 'c', 'd'])
# print(my_series2['d'])
# print(my_series2[:'d'])

# #Dataframe
# df = pd.DataFrame({
#     'country':["Russia", "Belarus", "Kazahstan"],
#     'population': [17.04, 20.07, 45.5 ],
#     'squre': [27224904, 17125191, 603628]},
#     index=['RU', 'BY', 'KZ']
# )
#
# print(df.columns)
# Index([u'country', u'population', u'squre'], dtype= 'object')
# print(df.index)
# RangeIndex(start=0, stop=4, step=1)


# print(df)



# df = pd.DataFrame(np.random.randn(8, 3), index=pd.date_range('1/1/2000', periods=8), columns=['A', 'B', 'C'])

# wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],major_axis=pd.date_range('1/1/2000', periods=5),minor_axis=['A', 'B', 'C', 'D'])
#
# print(wp)
# Загрузите файл.
# Выведите первые 5 строк.
# Выведите средние арифметические, минимумы и максимумы по всем колонкам.

data2 = pd.read_excel('D:\\filename.xlsx', sheetname='1') #загрузка и чтение файла xls
data3 = pd.read_csv('D:\\Competitions\\Rossman\\train.csv') #чтение файла


data = pd.read_csv('C:/Users/user/Desktop/2.2 cereal.csv', sep=';', decimal=',')##загрузка и чтение файла xls
data.to_csv('2.2 cereal.csv') #сохранение








