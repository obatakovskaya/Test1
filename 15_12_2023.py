import pandas as pd
import numpy as np
a, b, c = 1, 2 ,3
a = 2

# Exel
# data = pd.read_excel('C:\Users\user\Desktop\titanic.xlsx', sheetname='1')
# csv-файл
# data = pd.read_csv('D:\\filename.csv', sep=';', decimal=',')
# data.to_csv('filename.csv') # сохранение

# # простейшие операции
# # столбцы
# titanic_df = pd.read_csv('titanic.csv')
# print(titanic_df.columns)
#
# # строки - но тут временная индексация
# print(titanic_df.index)
#
# # сортировка
# print(titanic_df.sort_values(by='PClass'))

# Удаления
# df = pd.DataFrame({'x': [1, 3, 2], 'y': [2, 4, 1]})
# print(df)

# удаление строки
# df.drop(2, axis=0, inplace=True)
# print(df)
# # удаление столбца
# del df['x'] # df.drop('x', axis=1)
# print(df)

# df1 = pd.DataFrame({'x':[1,3,2], 'y':[2,4,1]})
# df2 = pd.DataFrame({'x':[3,1,2], 'y':[0,2,2]})
# print(df1>=df2)
#
# print((df1 >= df2).all())
#
# print((df1>=df2).any())


# Несколько колонок как функция одной

# a = pd.DataFrame({'a': [1,2,1,2], 'b':[3,3,3,4]})
# def two_three_strings(x):
#     return x*2, x*3
# a['twice'], a['thrice'] = zip(*a['a'].map(two_three_strings))
# print(a)

# Одна колонка как функция нескольких
# Из имени и фамилии делаем полное имя

df = pd.DataFrame({'name': [u'Маша', u'Саша', u'Рудольф'], 'surname':[u'Петрова', u'Сидоров', u'Кац']})
# первый способ
lst = []
for n, s in zip(df.name, df.surname):
    lst.append(n + ' ' + s)
# df['fullname'] = lst
# df['fullname2'] = df[['name', 'surname']].apply(lambda x: x[0] + ' ' + x[1], axis=1)
df['fullname3'] = df['name'] + ' ' + df['surname']

print(df)

# Задание
# В предложенном наборе данных:
# Отсортируйте его по возрастанию столбца «номер клиента».
# Заполните пропущенный возраст клиентов средним возрастом по набору.








