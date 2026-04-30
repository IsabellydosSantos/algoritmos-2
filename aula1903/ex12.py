def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    transposta_matriz = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta_matriz.append(nova_linha)
    
    return transposta_matriz


def quadrada(matriz):
    if not matriz:
        return False
    
    nlinhas = len(matriz)
    for linha in matriz:
        if len(linha) != nlinhas:
            return False
    return True


def simetrica(matriz):
    if not quadrada(matriz):
        print("A matriz não é quadrada, logo, não pode ser simétrica")
        return False
    
    mtransposta = transposta(matriz)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != mtransposta[i][j]:
                print(f"Há diferença nas matrizes em [{i}][{j}]")
                return False
    
    print("A matriz é simétrica")
    return True


# Entrada da matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
print(f"\nDigite os elementos da matriz {linhas}x{colunas}:")

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
        linha.append(elemento)
    matriz.append(linha)

print("\nMatriz original:")
for linha in matriz:
    print(linha)

matriz_transposta = transposta(matriz)

print("\nMatriz transposta:")
for linha in matriz_transposta:
    print(linha)

simetrica(matriz)
