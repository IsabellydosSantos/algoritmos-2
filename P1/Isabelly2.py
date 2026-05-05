def produto(A,B):
    linhas_A = len(A)
    colunas_A = len(A[0])
    linhas_B = len(B)
    colunas_B = len(B[0])

    if colunas_A != linhas_B:
        print("As dimensões não são compatíveis.")
        return None

    resultado = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


linhaA = int(input("Insira o número de linhas da Matriz A: "))
colunaA = int(input("Insira o número de colunas da Matriz A: "))

matrizA = []

for i in range(linhaA):
    linhasA = []
    for j in range(colunaA):
        valor = float(input(f"Insira o elemento [{i+1}][{j+1}]: "))
        linhasA.append(valor)
    matrizA.append(linhasA)


linhaB = int(input("Insira o número de linhas da Matriz B: "))
colunaB = int(input("Insira o número de colunas da Matriz B: "))

matrizB = []

for i in range(linhaB):
    linhasB = []
    for j in range(colunaB):
        valor = float(input(f"Insira o elemento [{i+1}][{j+1}]: "))
        linhasB.append(valor)
    matrizB.append(linhasB)

print("Matriz A")
for linha in matrizA:
    print(linha)

print("Matriz B")
for linha in matrizB:
    print(linha)

resultado = produto(matrizA,matrizB)

if resultado is not None:
    print("Produto das Matrizes A e B: ")
    for linha in resultado:
        print(linha)

