import pandas as pd
import numpy as np

# Veri yükleme
data = pd.read_csv('data.csv')

# Eksik değerler oluşturma
data.loc[0, 'Volume'] = np.nan
data.loc[1, 'Weight'] = np.nan
data.loc[2, 'CO2'] = np.nan

print("Eksik değerler eklenmiş veri:")
print(data)

# Sayısal sütunları seçme
numeric_columns = data.select_dtypes(include=[float, int]).columns

# Eksik değerleri sütunların ortalaması ile doldurma
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

print("Eksik değerleri doldurulmuş veri:")
print(data)
