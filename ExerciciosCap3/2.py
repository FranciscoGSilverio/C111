loja_1 = {"iphone", "galaxy", "ipad", "lg"}
loja_2 = {"iphone", "galaxy", "samsung", "redmi"}

total = len(loja_1.union(loja_2))
print(total)

comum = loja_1.intersection(loja_2)
print(comum)