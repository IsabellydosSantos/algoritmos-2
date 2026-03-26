def verificar_dimensoes(A, B):
    return len(A) == len(B) and len(A[0]) == len(B[0])

def soma(A, B):

    if not verificar_dimensoes(A, B):
        print("As dimensões são diferentes")
        return None


    linhas = len(A)
    colunas = len(A[0])

    resultado = [[A[i][j] + B[i][j] for j in range(colunas)] for i in range(linhas)]

    return resultado


linhasA = int(input("Informe o número de linhas da primeira matriz: "))
colunasA = int(input("Informe o número de colunas da primeira matriz: "))

matrizA = []

for i in range(linhasA):
    linha = []
    for j in range(colunasA):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matrizA.append(linha)


linhasB = int(input("Informe o número de linhas da segunda matriz: "))
colunasB = int(input("Informe o número de colunas da segunda matriz: "))

matrizB = []

for i in range(linhasB):
    linha = []
    for j in range(colunasB):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matrizB.append(linha)

resultado = soma(matrizA, matrizB)

print("Matriz A: \n")
for linha in matrizA:
    print(linha)

print("Matriz B: \n")
for linha in matrizB:
    print(linha)

print(f"Soma das matrizes A e B: {resultado}")

print("Matriz C: \n")
for linha in resultado:
    print(resultado)
    
