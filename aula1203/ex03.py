matriz =[]

for i in range(3):
    linha = []
    for j in range(4):
        linha.append((i+1) * (j+1))
    matriz.append(linha)

for linha in matriz:

    print(linha)

