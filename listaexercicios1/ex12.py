# Programa para encontrar a linha de maior soma em uma matriz 3x3

def ler_matriz():
    matriz = []
    print("Digite os elementos da matriz 3x3:")
    
    for i in range(3):
        linha = []
        print(f"\nLinha {i+1}:")
        for j in range(3):
            while True:
                try:
                    valor = int(input(f"  Elemento [{i+1}][{j+1}]: "))
                    linha.append(valor)
                    break
                except ValueError:
                    print("  Erro! Digite um número inteiro válido.")
        matriz.append(linha)
    
    return matriz

def encontrar_linha_maior_soma(matriz):
    maior_soma = -float('inf')  # Começa com o menor valor possível
    linha_maior = 0
    linha_valores = []
    
    for i in range(3):
        soma_linha = sum(matriz[i])  # Soma todos os elementos da linha i
        print(f"Soma da linha {i+1}: {soma_linha}")
        
        if soma_linha > maior_soma:
            maior_soma = soma_linha
            linha_maior = i + 1  # +1 porque o usuário vê linha 1,2,3
            linha_valores = matriz[i]
    
    return linha_maior, maior_soma, linha_valores

def imprimir_matriz(matriz):
    print("\n" + "=" * 40)
    print("MATRIZ DIGITADA:")
    print("=" * 40)
    for i in range(3):
        # Formata cada linha com 4 espaços para cada elemento
        linha_formatada = "  ".join(f"{matriz[i][j]:>4}" for j in range(3))
        print(f"Linha {i+1}: {linha_formatada}")


# Ler a matriz
matriz = ler_matriz()

# Imprimir a matriz
imprimir_matriz(matriz)

linha, soma, valores = encontrar_linha_maior_soma(matriz)

print(f"Linha com maior soma: Linha {linha}")
print(f"Valores da linha: {valores}")
print(f"Soma total: {soma}")
