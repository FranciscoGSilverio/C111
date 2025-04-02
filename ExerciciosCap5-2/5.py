import pandas as pd
import numpy as np

df = pd.read_csv('paises.csv', on_bad_lines='skip', encoding='latin1', delimiter=';', encoding_errors='ignore')

def classificar_mortalidade(mortalidade):
    if mortalidade < 9:
        return 'Balanced'
    else:
        return 'Urgent'

df['Humanitarian Help'] = df['Deathrate'].apply(classificar_mortalidade)
print("Dataset com a nova coluna 'Humanitarian Help':")
print(df[['ï»¿Country', 'Deathrate', 'Humanitarian Help']].to_string(index=False))
print("\n")
