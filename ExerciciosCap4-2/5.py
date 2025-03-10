import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype='str', encoding='utf-8')

companies = data[1:, 1]
uniqueCompanies = np.unique(companies)
missionsByCompany = np.array([(company, len(companies[companies == company])) for company in uniqueCompanies])

print('Número de missões por empresa:')
for company, missions in missionsByCompany:
    print(f'{company}: {missions} missões')
