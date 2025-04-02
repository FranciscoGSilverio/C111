import pandas as pd
import numpy as np

df = pd.read_csv('paises.csv', on_bad_lines='skip', encoding='latin1', delimiter=';', encoding_errors='ignore')

df_no_coast = df[df['Coastline (coast/area ratio)'] == 0]
df_no_coast.to_csv('noCoast.csv', index=False)
print("Países sem costa marítima:")
print(df_no_coast['ï»¿Country'].to_string(index=False))
print("\n")
