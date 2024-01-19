import pandas as pd
import numpy as np

df = pd.DataFrame({
    'country':['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 45.5],
    'square': [2724902, 17125191, 603628, 603628]})

print(type(df['country']))
print(df.columns)
