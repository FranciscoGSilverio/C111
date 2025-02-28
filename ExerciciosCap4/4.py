import numpy as np

matriz = np.random.randint(0, 10, (4, 5))  # Matriz 4x5
num_linhas, num_colunas = matriz.shape
num_elementos = num_linhas * num_colunas

paridade = "par" if num_elementos % 2 == 0 else "ímpar"

print("Matriz:")
print(matriz)
print(f"Número de elementos: {num_elementos} ({paridade})")
