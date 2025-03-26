import numpy as np
import pandas as pd

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

# 6.
media_x_menor_30 = df[df['X'] < 30]['X'].mean()
print(f"Média dos elementos da coluna X menores que 30: {media_x_menor_30:.2f}")

# 7.
media_linha_D = df.loc['D'].mean()
soma_linha_E = df.iloc[4].sum()
print(f"Média dos elementos da linha D: {media_linha_D:.2f}")
print(f"Soma dos elementos da linha E: {soma_linha_E}")

# 8. 
sliced_df = df.loc[['A', 'C', 'E'], ['X', 'Y']]
print("Slicing da matriz:")
print(sliced_df)
soma_por_linha = sliced_df.sum(axis=1)
soma_por_coluna = sliced_df.sum(axis=0)
print("Soma dos elementos por linha:")
print(soma_por_linha)
print("Soma dos elementos por coluna:")
print(soma_por_coluna)
