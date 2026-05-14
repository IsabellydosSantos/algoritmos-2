import random


def insertion_sort_baralho(baralho):
    total_comparacoes = 0
    
    for i in range(1, len(baralho)):
        carta_atual = baralho[i]
        posicao = i - 1
        
        print(f"\n {i}ª carta: {carta_atual}")
        print(f"   Cartas já ordenadas: {baralho[:i]}")
        
        while posicao >= 0 and comparar_cartas(baralho[posicao], carta_atual) > 0:
            print(f"   → {baralho[posicao]} > {carta_atual}, deslocando")
            
            baralho[posicao + 1] = baralho[posicao]
            posicao -= 1
            total_comparacoes += 1
        
        baralho[posicao + 1] = carta_atual
        
        print(f"   Insere {carta_atual} na posição {posicao + 1}")
        print(f"   Resultado: {baralho[:i+1]}")
    
    return baralho, total_comparacoes


def comparar_cartas(carta1, carta2):
    if carta1 == "🃏 Coringa":
        return 1
    if carta2 == "🃏 Coringa":
        return -1
    
    ordem_naipes = {'ouros': 0, 'paus': 1, 'copas': 2, 'espadas': 3}
    ordem_valores = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4,
                     '6': 5, '7': 6, '8': 7, '9': 8, '10': 9,
                     'J': 10, 'Q': 11, 'K': 12}
    
    conversor = {'Ás': 'A', 'Valete': 'J', 'Dama': 'Q', 'Rei': 'K'}
    
    parte1 = carta1.split(' de ')
    parte2 = carta2.split(' de ')
    
    valor1 = conversor.get(parte1[0], parte1[0])
    naipe1 = parte1[1]
    
    valor2 = conversor.get(parte2[0], parte2[0])
    naipe2 = parte2[1]
    
    if ordem_naipes[naipe1] != ordem_naipes[naipe2]:
        return ordem_naipes[naipe1] - ordem_naipes[naipe2]
    
    return ordem_valores[valor1] - ordem_valores[valor2]


def criar_baralho():
    naipes = ['ouros', 'paus', 'copas', 'espadas']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    nomes = {'A': 'Ás', 'J': 'Valete', 'Q': 'Dama', 'K': 'Rei'}
    
    baralho = []
    for naipe in naipes:
        for valor in valores:
            nome_valor = nomes.get(valor, valor)
            baralho.append(f"{nome_valor} de {naipe}")
    
    baralho.append("🃏 Coringa")
    return baralho


def formatar_carta(carta):
    if "🃏" in carta:
        return "🃏"
    
    partes = carta.split(' de ')
    valor = partes[0]
    naipe = partes[1]
    
    abrev_valor = {'Ás': 'A', 'Valete': 'J', 'Dama': 'Q', 'Rei': 'K'}
    valor_abrev = abrev_valor.get(valor, valor)
    
    simbolos = {'ouros': '♦', 'paus': '♣', 'copas': '♥', 'espadas': '♠'}
    simbolo = simbolos[naipe]
    
    if valor_abrev == '10':
        return f"10{simbolo}"
    return f"{valor_abrev}{simbolo}"


def mostrar_baralho(baralho, titulo, colunas=13):
    print(f"\n{titulo}")
    
    for i, carta in enumerate(baralho):
        carta_formatada = formatar_carta(carta)
        print(f"{carta_formatada:>3}", end=" ")
        
        if (i + 1) % colunas == 0:
            print()
    
    if len(baralho) % colunas != 0:
        print()
    
    print(f"Total: {len(baralho)} cartas")


print("Organizador de baralhos")

print("\n Criando baralho")
baralho = criar_baralho()
mostrar_baralho(baralho, " Baralho criado: ", colunas=13)

print("\n Embaralhando")
random.shuffle(baralho)
mostrar_baralho(baralho, " Baralho embaralhado: ", colunas=13)

print("\n Ordenando com Insertion Sort")
baralho_ordenado, comparacoes = insertion_sort_baralho(baralho.copy())

mostrar_baralho(baralho_ordenado, "Baralho ordenado", colunas=13)
