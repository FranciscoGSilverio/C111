#load csv
import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')

missionStatus = data[:, 7]
successfullMissions = missionStatus[missionStatus == 'Success']

successPercentage = (len(successfullMissions) / len(missionStatus)) * 100

print(f'{successPercentage:.2f}% das missões foram bem sucedidas')