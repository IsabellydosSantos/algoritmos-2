def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor_ind = i
        print(f"{i+1}° passo: Procura o menor elemento a partir do elemento {i}\n")
        print(f"Sub-lista não ordenada: {lista[i:]}\n")
        for j in range(i+1, n):
            if lista[j] < lista[menor_ind]:
                menor_ind = j
                print(f"Novo menor número encontrado: {lista[j]} na posição {j}\n")
        if menor_ind != 1:
            print(f"Trocando {lista[i]} (posição {i}) com {lista[menor_ind]} (posição {menor_ind})\n")
            lista[i], lista[menor_ind] = lista[menor_ind], lista[i]
        else:
            print(f"{lista[i]} já está na posição correta\n")
        print(f"Lista após {i+1}° passo: {lista}\n")
    return lista


L = [14, 7, 8, 34, 56, 4, 0, 9, -8, 100]

lista_ord = selection_sort(L.copy())
print(f"Lista ordenada: {lista_ord}")
