import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')

location = data[1:, 2]
byUSA = location[np.char.find(location, 'USA') != -1]

print(f'{len(byUSA)} missões foram realizadas pelos Estados Unidos')