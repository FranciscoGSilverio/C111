numero_usr = input("Digite um número: ")
intervalo_inicio = input("Digite um intervalo (1 a 10): ")
intervalo_fim = input("Digite um intervalo (1 a 10): ")

numero = int(numero_usr)

for i in range(int(intervalo_inicio), int(intervalo_fim)+1):
    print(numero, "x", i, "=", numero*i)
    if i == intervalo_fim:
        break
    else:
        continue

