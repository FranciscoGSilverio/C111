import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')

company_cost = data[1:, [1, 6]]
spaceX = company_cost[company_cost[:, 0] == 'SpaceX']
max_cost = np.max(spaceX[:, 1].astype(float))


print(f'O maior custo de uma missão da SpaceX foi de {max_cost:.2f} milhões de dólares')