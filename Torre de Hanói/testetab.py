#pip install tabulate
import time
import os
from tabulate import tabulate  # Biblioteca para fazer tabelas bonitas

# Cores do arco-íris para os 8 discos (ANSI escape codes)
CORES = {
    1: '\033[91m',      # 1 = Vermelho
    2: '\033[38;5;208m', # 2 = Laranja  
    3: '\033[93m',      # 3 = Amarelo
    4: '\033[92m',      # 4 = Verde
    5: '\033[94m',      # 5 = Azul
    6: '\033[96m',      # 6 = Anil (Ciano)
    7: '\033[95m',      # 7 = Violeta (Roxo)
    8: '\033[38;5;201m' # 8 = Magenta (Rosa)
}
RESET = '\033[0m'  # Volta à cor padrão do terminal

def disco_colorido(numero, tamanho_maximo):
    """Desenha um disco com tamanho proporcional ao número"""
    tamanho = numero * 2 - 1  # Disco 1 = 1 bloco, Disco 8 = 15 blocos
    cor = CORES.get(numero, '\033[97m')  # Pega a cor do disco
    
    # Coloca o número do disco no centro (se o disco for grande o suficiente)
    disco = "█" * tamanho  # Cria a barra do disco
    if tamanho >= 3:
        pos = tamanho // 2  # Posição central
        # Insere o número no meio da barra
        disco = disco[:pos] + str(numero) + disco[pos+1:]
    
    return cor + disco + RESET  # Retorna o disco colorido

def mostrar_jogo(hastes, n, movimentos, inicio):
    """Mostra o estado atual do jogo na tela"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela (Windows ou Linux/Mac)
    
    # ========== CABEÇALHO ==========
    print("=" * 70)
    print(f" TORRE DE HANÓI - {n} DISCOS ".center(70))
    print("=" * 70)
    
    # ========== ESTATÍSTICAS ==========
    progresso = len(hastes['C']) / n * 100  # % de discos na haste C
    tempo = int(time.time() - inicio)  # Tempo decorrido em segundos
    
    # Tabela de estatísticas (tabulate)
    stats = [
        ["Movimentos", movimentos],
        ["Mínimo teórico", 2**n - 1],
        ["Progresso", f"{progresso:.0f}%"],
        ["Tempo", f"{tempo//60:02d}:{tempo%60:02d}"]
    ]
    print(tabulate(stats, tablefmt="simple"))
    print()
    
    # ========== BARRA DE PROGRESSO ==========
    barras = int(progresso / 100 * 40)
    print(f"[{'█' * barras}{'░' * (40 - barras)}] {progresso:.0f}%")
    print()
    
    # ========== DESENHO DAS HASTES ==========
    tabela_hastes = []  # Lista que vai virar a tabela
    
    # Percorre de cima para baixo (do nível mais alto até a base)
    for nivel in range(n-1, -1, -1):
        linha = []  # Uma linha da tabela (um nível das 3 hastes)
        
        for haste in ['A', 'B', 'C']:  # Para cada haste
            if nivel < len(hastes[haste]):  # Se tem disco neste nível
                disco = hastes[haste][nivel]
                linha.append(disco_colorido(disco, n))  # Desenha o disco colorido
            else:
                linha.append("|")  # Haste vazia mostra apenas |
        
        tabela_hastes.append(linha)
    
    # Adiciona a base das hastes (linha do chão)
    base = ["═" * (n*2 - 1), "═" * (n*2 - 1), "═" * (n*2 - 1)]
    tabela_hastes.append(base)
    
    # Exibe a tabela das hastes
    print(tabulate(tabela_hastes, headers=["A", "B", "C"], tablefmt="grid"))
    
    # ========== DICA E COMANDOS ==========
    print(f"\n💡 Dica: {dica(hastes, n)}")
    print("Comandos: A B (ex: A C) | Q para sair")

def dica(hastes, n):
    """Dá uma dica simples baseada no estado atual"""
    if len(hastes['C']) == n:
        return "VOCÊ VAI VENCER! Faça o último movimento!"
    elif len(hastes['A']) == n:
        return f"Primeiro movimento: leve o disco 1 para B ou C"
    elif hastes['B'] and hastes['B'][-1] == 1:
        return "Use o disco 1 (está em B) como base"
    else:
        return "Coloque discos menores sobre maiores"

def valido(hastes, origem, destino):
    """Verifica se o movimento é permitido pelas regras"""
    if not hastes[origem]:  # Haste de origem está vazia?
        print("❌ Haste origem vazia!")
        return False
    
    disco_origem = hastes[origem][-1]  # Pega o disco do topo da origem
    
    if hastes[destino]:  # Se a haste destino tem disco(s)
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:  # Disco maior sobre menor?
            print("❌ Não pode colocar disco maior sobre menor!")
            return False
    
    return True  # Movimento permitido

def legenda(n):
    """Mostra a legenda com as cores de cada disco"""
    print("\n📖 LEGENDA:")
    for i in range(1, n+1):
        print(f"  Disco {i}: {disco_colorido(i, n)}")

def jogar():
    """Função principal do jogo"""
    print("=" * 70)
    print(" TORRE DE HANÓI ".center(70))
    print("=" * 70)
    
    # Entrada do usuário
    n = int(input("\nNúmero de discos (1-8): "))
    if n < 1 or n > 8:
        print("Digite um número entre 1 e 8")
        return
    
    # Inicialização do jogo
    hastes = {
        'A': list(range(n, 0, -1)),  # A começa com todos os discos (maior embaixo)
        'B': [],  # B começa vazia
        'C': []   # C começa vazia
    }
    
    movimentos = 0
    inicio = time.time()
    
    # Mostra a legenda e aguarda o jogador
    legenda(n)
    input("\nPressione ENTER para começar...")
    
    # LOOP PRINCIPAL DO JOGO
    while hastes['C'] != list(range(n, 0, -1)):  # Enquanto não ganhou
        mostrar_jogo(hastes, n, movimentos, inicio)
        
        # Entrada do jogador
        cmd = input("\n> ").upper().strip()
        if cmd == 'Q':
            print("Jogo encerrado!")
            return
        
        # Processa o comando (ex: "A C")
        partes = cmd.split()
        if len(partes) != 2:
            print("Use: ORIGEM DESTINO (ex: A C)")
            time.sleep(1)
            continue
        
        origem, destino = partes[0], partes[1]
        
        # Validação básica
        if origem not in 'ABC' or destino not in 'ABC':
            print("Use apenas A, B ou C")
            time.sleep(1)
            continue
        
        # Se o movimento é válido pela regra do jogo
        if valido(hastes, origem, destino):
            disco = hastes[origem].pop()  # Remove o disco da origem
            hastes[destino].append(disco)  # Coloca na destino
            movimentos += 1
            print(f"\n✅ Movimento {movimentos}: {origem} → {destino}")
            time.sleep(0.3)
    
    # VITÓRIA!
    mostrar_jogo(hastes, n, movimentos, inicio)
    print("\n" + "🎉" * 35)
    print(" PARABÉNS! VOCÊ VENCEU! ".center(70))
    print("🎉" * 35)

# Inicia o jogo
if __name__ == "__main__":
    jogar()
