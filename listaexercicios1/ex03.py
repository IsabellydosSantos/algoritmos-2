dist = float(input("Qual a distância que deseja percorrer (em KM)? "))

if dist <= 200:
    preco = dist * 0.50
    print(f"O preço da passagem é igual a RS{preco}")
else:
    preco = dist * 0.45
    print(f"O preço da passagem é igual a RS{preco}")
