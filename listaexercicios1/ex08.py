# Programa para somar duas listas elemento por elemento usando ZIP

print("=" * 50)
print("SOMADOR DE LISTAS")
print("=" * 50)

# Receber a primeira lista
entrada1 = input("\nDigite os números da primeira lista (separados por vírgula): ")
lista1 = [float(x.strip()) for x in entrada1.split(',')]

# Receber a segunda lista
entrada2 = input("Digite os números da segunda lista (separados por vírgula): ")
lista2 = [float(x.strip()) for x in entrada2.split(',')]

# Verificar se as listas têm o mesmo tamanho
if len(lista1) != len(lista2):
    print("\n⚠️ ATENÇÃO: As listas têm tamanhos diferentes!")
    print(f"Lista 1: {len(lista1)} elementos")
    print(f"Lista 2: {len(lista2)} elementos")
    
    # Completar a menor lista com zeros
    tamanho_max = max(len(lista1), len(lista2))
    
    while len(lista1) < tamanho_max:
        lista1.append(0)
    while len(lista2) < tamanho_max:
        lista2.append(0)
    
    print(f"\n✓ Listas ajustadas para {tamanho_max} elementos (preenchidas com zeros)")
    print(f"Lista 1 ajustada: {lista1}")
    print(f"Lista 2 ajustada: {lista2}")

# ========== MUDANÇA AQUI ==========
# ANTIGO (sem zip):
# lista_soma = []
# for i in range(len(lista1)):
#     soma = lista1[i] + lista2[i]
#     lista_soma.append(soma)

# NOVO (com zip) - MUITO MAIS LIMPO!
lista_soma = [a + b for a, b in zip(lista1, lista2)]
# ===================================

# Exibir os resultados
print("\n" + "=" * 50)
print("RESULTADOS")
print("=" * 50)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista soma: {lista_soma}")

# ========== OUTRA MUDANÇA AQUI ==========
# Exibir soma detalhada usando ZIP também
print("\n" + "-" * 50)
print("Soma elemento por elemento:")

# ANTIGO (sem zip):
# for i in range(len(lista1)):
#     print(f"  {lista1[i]} + {lista2[i]} = {lista_soma[i]}")

# NOVO (com zip) - MAIS LEGÍVEL
for a, b in zip(lista1, lista2):
    print(f"  {a} + {b} = {a + b}")
# =========================================
