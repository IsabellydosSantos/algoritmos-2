def criar_lista():
    while True:
        try:
            entrada = input("Digite os números (separados por vírgula): ")
            valores = [x.strip() for x in entrada.split(',')]
            lista = [int(valor) for valor in valores]
            return lista
        except ValueError:
            print("Insira apenas números inteiros separados por vírgula.")


lista = criar_lista()

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()

# Estatísticas
total_pares = len(pares)
total_impares = len(impares)
total_numeros = len(lista)

print(f"\nLista original ({total_numeros} números):")
print(f"   {lista}")

print(f"\nNúmeros Pares ({total_pares} números):")
if pares:
    print(f"   {pares}")
    print(f"   Soma: {sum(pares)}")
    print(f"   Média: {sum(pares)/len(pares):.2f}")
else:
    print("   Nenhum número par encontrado")

print(f"\nNúmeros Ímpares ({total_impares} números):")
if impares:
    print(f"   {impares}")
    print(f"   Soma: {sum(impares)}")
    print(f"   Média: {sum(impares)/len(impares):.2f}")
else:
    print("   Nenhum número ímpar encontrado")

