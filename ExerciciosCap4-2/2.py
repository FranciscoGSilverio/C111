import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')

cost = data[1:, 6].astype(float)

availableCosts = cost[cost > 0]

averageCost = np.mean(availableCosts)
print(f'O custo médio das missões é de {averageCost:.2f} milhões de dólares')

