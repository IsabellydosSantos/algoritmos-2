def soma_diag(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma


n = int(input("Insira o tamanho da matriz quadrada: "))

matriz = []
print("Insira os elementos da matriz: ")
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

    print("Matriz: ")
    for linha in matriz:
        print(linha)

    resultado = soma_diag(matriz)
    print(f"Somatório da diagonal principal: {resultado}")
