import pandas as pd
import numpy as np

df = pd.read_csv('paises.csv', on_bad_lines='skip', encoding='latin1', delimiter=';', encoding_errors='ignore')

oceania = df[df['Region'].str.contains('OCEANIA')]

countries_oceania = oceania['ï»¿Country'].tolist()
print("Países da OCEANIA:")
for country in countries_oceania:
    print(country)

print("\n")

num_paises_oceania = len(oceania)
print(f"Número de países da OCEANIA: {num_paises_oceania}")
print("\n")

