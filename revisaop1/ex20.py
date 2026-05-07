def matriz_identidade(matriz):
    n = len(matriz)

    for linha in matriz:
        if len(linha) != n:
            print("A matriz deve ser quadrada")

    for i in range(n):
        for j in range(n):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False
    return True


n = int(input("Insira o número de linhas da matriz quadrada: "))

matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = float(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

if matriz_identidade(matriz):
    print("É uma matriz identidade")
else:
    print("Não é uma matriz identidade")

