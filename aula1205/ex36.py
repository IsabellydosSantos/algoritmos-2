def bubble_sort(lista):
    n = len(lista)

    for i in range(n-1):
        trocou = False

        for j in range(0, n-i-1):
            print(f"Comparando {lista[j]} e {lista[j+1]}")
            if lista[j] > lista[j+1]:
                print(f"{lista[j]} > {lista[j + 1]}, troca")
                