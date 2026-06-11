def busca_sequencial(lista,chave):
    posicoes = []

    for i in range(len(lista)):
        if lista[i] == chave:
            posicoes.append(i)
    if posicoes:
        return posicoes
    else:
        return f"Erro: A chave '{chave}' não foi encontrada na lista"


def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    prim_posic = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            prim_posic = meio
            break
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    if prim_posic == -1:
        return f"Erro: A chave '{chave}' não foi encontrada na lista"
        
