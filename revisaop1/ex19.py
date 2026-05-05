def menor_elem(matriz):
    return min(min(linha) for linha in matriz)


linhas = int(input("Insira o número de linhas da matriz: "))
colunas = int(input("Insira o número de colunas da matriz: "))

matriz = []
for i in range(linhas):
    linha = list(map(float, input(f"Linha {i+1} (digite {colunas} números separados por vígula: ").strip().split(',')))
    matriz.append(linha)

print(f"Menor elemento da matriz: {menor_elem(matriz)}")

