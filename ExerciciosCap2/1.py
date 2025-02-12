name = input("What is your name? ")

upper = name.upper()
print("Em letras maiúsculas: ")
print(upper)

lower = name.lower()
print("Em letras minúsculas: ")
print(lower)

print("Quantidade de caracteres: ")
count = len(name)

print("Último nome substituído por 'do Inatel': ")
last_name = name.split()[-1]
replace = name.replace(last_name, "do Inatel")
print(replace)
