# Programa para somar duas listas elemento por elemento

entrada1 = input("Insira os números da primeira lista (separados por vírgula): ")
lista1 = [float(x.strip()) for x in entrada1.split(',')]

entrada2 = input("Insira os números da segunda lista (separados por vírgula): ")
lista2 = [float(x.strip()) for x in entrada2.split(',')]

if len(lista1) != len(lista2):
    print("\nAs listas têm tamanhos diferentes")
        
    # Completar a menor lista com zeros
    tamanho_max = max(len(lista1), len(lista2))
    
    while len(lista1) < tamanho_max:
        lista1.append(0)
    while len(lista2) < tamanho_max:
        lista2.append(0)
    
lista_soma = [a + b for a, b in zip(lista1, lista2)]

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista soma: {lista_soma}")
