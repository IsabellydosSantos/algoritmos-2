def verificar_dimensoes(A, B):
    return len(A[0]) == len(B)

def multiplicacao(A, B):

    if not verificar_dimensoes(A, B):
        print("As dimensões não são compatívei")
        return None


    linhasA = len(A)
    colunasA = len(A[0])
    colunasB = len(B[0])


    resultado = []

    for i in range(linhasA):
        linha_resultado = []
        for j in range(colunasB):
            soma = 0
            print(f"C[{i+1}][{j+1}] = ")

            for k in range(colunasA):
                produto = A[i][k] * B[k][j]
                soma += produto
                print(f"{A[i][k]}×{B[k][j]} ")
                if k < colunasA - 1:
                    print(" + ")
            print(f" = {soma}")
            linha_resultado.append(soma)
        resultado.append(linha_resultado)

     return resultado


linhasA = int(input("Informe o número de linhas da primeira matriz: "))
colunasA = int(input("Informe o número de colunas da primeira matriz: "))

matrizA = []

for i in range(linhasA):
    linha = []
    for j in range(colunasA):
        elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matrizA.append(linha)


linhasB = int(input("Informe o número de linhas da primeira matriz: "))
colunasB = int(input("Informe o número de colunas da primeira matriz: "))

matrizB = []

for i in range(linhasB):
    linha = []
    for j in range(colunasB):
        elemento = float(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matrizB.append(linha)

resultado = soma(matrizA, matrizB)

print(f"Produto das matrizes A e B: {resultado}")
