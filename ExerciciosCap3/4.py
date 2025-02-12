lista_pessoas = []

while len(lista_pessoas) < 3:
    nome = input("Digite o nome da pessoa: ")
    peso = int(input("Digite o peso da pessoa: "))
    lista_pessoas.append((nome, peso))

mais_pesado = max(lista_pessoas, key=lambda x: x[1])
print(f"O mais pesado é {mais_pesado[0]} com {mais_pesado[1]}kg")