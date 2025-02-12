lista_pessoas = []

while True:
    nome = input("Digite o nome da pessoa: ")
    if(nome == 'sair'):
        break
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")
    lista_pessoas.append((nome, idade, sexo))


media_idade = sum([x[1] for x in lista_pessoas]) / len(lista_pessoas)
print(f"A média de idade é {media_idade}")

mulheres = [x for x in lista_pessoas if x[2] == 'F' and x[1] < 20]
print(f"Mulheres com menos de 20 anos: {mulheres}")

