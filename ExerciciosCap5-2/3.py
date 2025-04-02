import pandas as pd
import numpy as np

df = pd.read_csv('paises.csv', on_bad_lines='skip', encoding='latin1', delimiter=';', encoding_errors='ignore')

# Agrupando os países por região e calculando a média de alfabetização
media_alfabetizacao = df.groupby('Region')['Literacy (%)'].mean()
print("Média de alfabetização por região:")
print(media_alfabetizacao)
print("\n")
