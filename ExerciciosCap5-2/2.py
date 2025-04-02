import pandas as pd
import numpy as np

df = pd.read_csv('paises.csv', on_bad_lines='skip', encoding='latin1', delimiter=';', encoding_errors='ignore')
print(df.columns)
df['Population'] = pd.to_numeric(df['Population'], errors='coerce')

most_populous_country = df.loc[df['Population'].idxmax(), 'ï»¿Country']
largest_population = df['Population'].max()

print(f"País com a maior população: {most_populous_country} com {largest_population:,} habitantes.")
