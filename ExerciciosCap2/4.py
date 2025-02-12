distancia_str = input("Digite a distância em km: ")

distancia = int(distancia_str)
preco = 0
if(distancia <=  200):
    preco = distancia * 0.5

else:
    preco = distancia * 0.45


print("Preço final: R$", preco)