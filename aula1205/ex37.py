def insertion_sort(lista):
    n = len(lista)
    
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        
        print(f"\n▶ PASSO {i}: Inserir o elemento {chave} (posição {i})")
        print(f"   Sub-lista ordenada: {lista[:i]}")
        print(f"   Sub-lista restante: {lista[i:]}")
        
        deslocamentos = 0
        
        while j >= 0 and lista[j] > chave:
            print(f"   → {lista[j]} > {chave}, desloco {lista[j]} para direita")
            lista[j + 1] = lista[j]
            deslocamentos += 1
            j -= 1
        
        posicao_insercao = j + 1
        lista[posicao_insercao] = chave
        
        if deslocamentos > 0:
            print(f"  Insere {chave} na posição {posicao_insercao}")
            print(f"  Deslocamentos realizados: {deslocamentos}")
        else:
            print(f"   {chave} já está na posição correta (nenhum deslocamento)")
        
        print(f" Lista atual: {lista}")
      
    return lista


entrada = input("Insira os elementos da lista (separados por vírgula: ")

try:
    lista = [int(x) for x in entrada.split(',')]

    if len(lista) == 0:
        print("\n Nenhum número foi inserido.")
    else:
        lista_ordenada = insertion_sort(L.copy())
        print(f" Lista ordenada: {lista_ordenada}")
except ValueError:
    print("\n Insira apenas números inteiros separados por vírgulas")
  
