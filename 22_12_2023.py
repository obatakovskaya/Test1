import numpy as np
import pandas as pd

# contries_client = pd.read_csv('clients_contries.csv')
#
# contries_client['fullname_age'] = contries_client['name'] + ' ' + contries_client['age'].astype(str)
# del contries_client['name']
# del contries_client['age']
# print(contries_client.head(10))

# autos_path = '2.4 autos.csv'
# autos_df = pd.read_csv(autos_path, encoding='koi8-r')
#
#
# autos_df["displacement"] = (np.pi * ((0.5 * autos_df.bore) ** 2) * autos_df.stroke * autos_df.num_of_cylinders)
# autos_df['make+fuel'] = autos_df['make'] + ': ' + autos_df['fuel_type']
# print(autos_df.head(10))

# Добавьте в датафрейм новые колонки:
# LivLotRatio как отношение колонки GrLivArea к колонке LotArea
# Spaciousness: сумма FirstFlrSF и SecondFlrSF, деленая на TotRmsAbvGrd
# Посмотрите на датафрейм, подумайте, какие ещё значения могут быть полезны, запишите одну из своих идей.

houses_df = pd.read_csv('2.4 houses.csv')
houses_df['LivLotRatio'] = houses_df['GrLivArea'] / houses_df['LotArea']
houses_df['Spaciousness'] = houses_df['FirstFlrSF'] + houses_df['SecondFlrSF'] / houses_df['TotRmsAbvGrd']
# print(houses_df.head(5))
# # print(houses_df.index)
# print(houses_df.iloc[2928])
# print(houses_df['LivLotRatio'])

# houses_df['fullname2'] = houses_df[['GrLivArea', 'LotArea']].apply(lambda x: x[0] + ' ' +x[1], axis=1)


print(houses_df.tail(10))

