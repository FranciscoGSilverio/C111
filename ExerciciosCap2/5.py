numero = input("Digite um número entre 1000 e 9999: ")

while int(numero) < 1000 or int(numero) > 9999:
    print("Número inválido")
    numero = input("Digite um número entre 1000 e 9999: ")
    
print("Número da unidade", numero[-1])
print("Número da dezena", numero[-2])
print("Número da centena", numero[-3])
print("Número do milhar", numero[-4])