import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))

media_linhas = np.mean(matriz, axis=1)
media_colunas = np.mean(matriz, axis=0)

maior_media_linhas = np.max(media_linhas)
maior_media_colunas = np.max(media_colunas)

valores, contagens = np.unique(matriz, return_counts=True)

numeros_2x = valores[contagens == 2]

print("Matriz:")
print(matriz)
print("\nMédia de cada linha:", media_linhas)
print("Média de cada coluna:", media_colunas)
print("\nMaior média das linhas:", maior_media_linhas)
print("Maior média das colunas:", maior_media_colunas)
print("\nContagem de aparições de cada número:")
for valor, contagem in zip(valores, contagens):
    print(f"Número {valor}: {contagem} vez(es)")
print("\nNúmeros que aparecem exatamente 2 vezes:", numeros_2x)
