def bubble_sort(lista):
    n = len(lista)

    for i in range(n-1):
        print(f"\n {i+1}° Iteração")
        troca = False

        for j in range(0, n-i-1):
            print(f"Comparando {lista[j]} e {lista[j+1]}")
            if lista[j] > lista[j+1]:
                print(f"{lista[j]} > {lista[j + 1]}, trocando")
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca = True
                print(f"→ Lista: {lista}")
            else:
                print(f"→ {lista[j]} < {lista[j+1]}, mantém → Lista: {lista}")
        print("Fim da {i+1}° Iteração: {lista}")

        if not troca:
            print("\n Nenhuma troca nesta iteração. A lista já está ordenada")
            break
    return lista


entrada = input("Insira os elementos da lista (separados por vírgula: ")

try:
    lista = [int(x) for x in entrada.split(',')]

    if len(lista) == 0:
        print("\n Nenhum número foi inserido.")
    else:
        lista_ordenada = bubble_sort(L.copy())
        print(f" Lista ordenada: {lista_ordenada}")
except ValueError:
    print("\n Insira apenas números inteiros separados por vírgulas")
    
