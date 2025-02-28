import numpy as np

array_pares_1 = np.arange(0, 52, 2)
array_pares_2 = np.arange(100, 48, -2)

array_concatenado = np.concatenate((array_pares_1, array_pares_2))
array_ordenado = np.sort(array_concatenado)

print("Array concatenado ordenado:", array_ordenado)
