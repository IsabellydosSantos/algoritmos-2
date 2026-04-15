def criar_lista():
    """Função para criar lista com tratamento de erros"""
    while True:
        try:
            entrada = input("Digite os números (separados por vírgula): ")
            # Remove espaços e separa por vírgula
            valores = [x.strip() for x in entrada.split(',')]
            # Converte para inteiros
            lista = [int(valor) for valor in valores]
            return lista
        except ValueError:
            print("Erro! Digite apenas números inteiros separados por vírgula.")
            print("Exemplo: 1,2,3,4,5\n")

# Programa principal
print("=" * 60)
print("SEPARADOR DE NÚMEROS PARES E ÍMPARES")
print("=" * 60)
print("\nInstruções:")
print("- Digite números inteiros separados por vírgula")
print("- Números negativos também são válidos")
print("- Exemplo: 1,2,3,4,5 ou -5,-4,-3,-2,-1\n")

# Receber a lista
lista = criar_lista()

# Separar pares e ímpares
pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Ordenar as listas (opcional)
pares.sort()
impares.sort()

# Estatísticas
total_pares = len(pares)
total_impares = len(impares)
total_numeros = len(lista)

# Exibir resultados formatados
print("\n" + "=" * 60)
print("RESULTADOS")
print("=" * 60)

print(f"\n📊 Lista original ({total_numeros} números):")
print(f"   {lista}")

print(f"\n✅ Números PARES ({total_pares} números):")
if pares:
    print(f"   {pares}")
    print(f"   Soma: {sum(pares)}")
    print(f"   Média: {sum(pares)/len(pares):.2f}")
else:
    print("   Nenhum número par encontrado")

print(f"\n🟢 Números ÍMPARES ({total_impares} números):")
if impares:
    print(f"   {impares}")
    print(f"   Soma: {sum(impares)}")
    print(f"   Média: {sum(impares)/len(impares):.2f}")
else:
    print("   Nenhum número ímpar encontrado")

# Porcentagem
if total_numeros > 0:
    print(f"\n📈 Porcentagem:")
    print(f"   Pares: {(total_pares/total_numeros)*100:.1f}%")
    print(f"   Ímpares: {(total_impares/total_numeros)*100:.1f}%")
