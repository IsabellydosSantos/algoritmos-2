matriz =[]

for i in range(3):
    linha = []
    for j in range(4):
        linha.append(i * j)
    matriz.append(linha)

for linha in matriz:
    print(linha)