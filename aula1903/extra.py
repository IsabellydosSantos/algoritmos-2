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

def transposta(matriz):
    if not matriz or not matriz[0]:
        return []
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    transposta_matriz = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta_matriz.append(nova_linha)
    
    return transposta_matriz

def soma_transposta(matrizA, matrizB):
    # Calcula as transpostas
    at = transposta(matrizA)
    bt = transposta(matrizB)
    
    print("\n" + "="*40)
    print("MATRIZ A^t (Transposta de A):")
    for linha in at:
        print(linha)
    
    print("\nMATRIZ B^t (Transposta de B):")
    for linha in bt:
        print(linha)
    
    # Soma as matrizes transpostas
    resultadost = soma(at, bt)
    
    return resultadost

# Entrada da primeira matriz
print("="*40)
print("PRIMEIRA MATRIZ")
print("="*40)
linhasA = int(input("Informe o número de linhas da primeira matriz: "))
colunasA = int(input("Informe o número de colunas da primeira matriz: "))

matrizA = []

for i in range(linhasA):
    linha = []
    for j in range(colunasA):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matrizA.append(linha)

# Entrada da segunda matriz
print("\n" + "="*40)
print("SEGUNDA MATRIZ")
print("="*40)
linhasB = int(input("Informe o número de linhas da segunda matriz: "))
colunasB = int(input("Informe o número de colunas da segunda matriz: "))

matrizB = []

for i in range(linhasB):
    linha = []
    for j in range(colunasB):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matrizB.append(linha)

# Exibindo as matrizes originais
print("\n" + "="*40)
print("MATRIZES ORIGINAIS")
print("="*40)
print("Matriz A:")
for linha in matrizA:
    print(linha)

print("\nMatriz B:")
for linha in matrizB:
    print(linha)

# Calculando a soma das transpostas
resultado_transpostas = soma_transposta(matrizA, matrizB)

# Exibindo o resultado final
if resultado_transpostas is not None:
    print("\n" + "="*40)
    print("RESULTADO: A^t + B^t")
    print("="*40)
    for linha in resultado_transpostas:
        print(linha)
else:
    print("\nNão foi possível realizar a soma das transpostas pois as dimensões são diferentes.")

