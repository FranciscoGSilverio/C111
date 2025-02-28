import numpy as np

array_ones = np.ones(8, dtype=int)
array_random = np.random.randint(0, 10, 8)
    
array_resultante = array_ones + array_random
    
soma_total = np.sum(array_resultante)
    
if soma_total >= 40:
    matriz_final = array_resultante.reshape(4, 2) 
else:
    matriz_final = array_resultante.reshape(2, 4)

print("Array de 1’s:", array_ones)
print("Array aleatório:", array_random)
print("Array resultante:", array_resultante)
print("Soma total:", soma_total)
print("Matriz final:")
print(matriz_final)