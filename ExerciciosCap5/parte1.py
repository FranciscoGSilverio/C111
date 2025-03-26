import pandas as pd

# 1. Criando as Series
year1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
year2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# 2. Calculando a porcentagem total de mercado
sum_year1 = year1.sum()
sum_year2 = year2.sum()
print(f"Total de mercado no Ano 1: {sum_year1:.2f}%")
print(f"Total de mercado no Ano 2: {sum_year2:.2f}%")

# 3. Calculando o crescimento/declínio de cada linguagem
growth = year2 - year1
print("\nCrescimento/Declínio de cada linguagem:")
print(growth)

# 4. Filtrando apenas linguagens que tiveram crescimento
growth_positive = growth[growth > 0]
print("\nLinguagens com crescimento:")
print(growth_positive)

# 5. Projetando crescimento para os próximos 2 anos
year3 = year2 + growth
year4 = year3 + growth
top_language = year4.nlargest(1)
print("\nLinguagem mais popular no Ano 4:")
print(top_language)