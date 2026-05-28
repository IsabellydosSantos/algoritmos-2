import time
import os

# Códigos de cor ANSI
CORES = {
    1: '\033[91m',  # Vermelho
    2: '\033[93m',  # Amarelo
    3: '\033[92m',  # Verde
    4: '\033[94m',  # Azul
    5: '\033[95m',  # Roxo
    6: '\033[96m',  # Ciano
    7: '\033[97m',  # Branco
    8: '\033[90m',  # Cinza (para disco 8)
}
RESET = '\033[0m'

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def disco_colorido(numero, tamanho_maximo):
    """Retorna disco colorido com tamanho proporcional"""
    tamanho = numero * 2 - 1
    cor = CORES.get(numero, '\033[97m')
    
    # Adiciona número no centro do disco se for grande o suficiente
    if tamanho >= 3:
        disco = "█" * tamanho
        pos = tamanho // 2
        # Ajustar posição do número para discos maiores
        if tamanho > 9:
            disco = disco[:pos-1] + str(numero) + disco[pos:]
        else:
            disco = disco[:pos] + str(numero) + disco[pos+1:]
    else:
        disco = "█" * tamanho
    
    return cor + disco + RESET

def disco_vazio(tamanho_maximo):
    """Retorna espaço vazio para haste sem disco"""
    espaco = " " * (tamanho_maximo * 2 - 1)
    return espaco

def desenhar_disco(disco_num, tamanho_maximo):
    """Desenha um único disco ou espaço vazio"""
    if disco_num == 0:
        return " " * (tamanho_maximo * 2 - 1)
    else:
        return disco_colorido(disco_num, tamanho_maximo)

def exibir_hastes_premium(hastes, n, movimentos, minimo_teorico, start_time):
    """Exibição ultra-detalhada do jogo com moldura de 90 caracteres"""
    
    tamanho_maximo = n
    largura_total = 90  # Moldura fixa de 90 caracteres
    
    # Calcular espaçamentos baseados no maior disco
    largura_disco_max = tamanho_maximo * 2 - 1
    espaco_por_haste = (largura_total - 6) // 3  # 6 = margens das laterais
    espaco_central = (espaco_por_haste - largura_disco_max) // 2
    
    # Moldura superior
    print("\n" + "╔" + "═" * largura_total + "╗")
    print("║" + " 🎮 TORRE DE HANÓI - EDIÇÃO PREMIUM 🎮 ".center(largura_total) + "║")
    print("╠" + "═" * largura_total + "╣")
    
    # Objetivo
    print(f"║ 🎯 Objetivo: Mover {n} discos de A → C".ljust(largura_total) + "║")
    print("╠" + "═" * largura_total + "╣")
    
    # Cabeçalho das hastes
    cabecalho = "║  "
    hastes_nomes = {'A': '🔴 A', 'B': '🟡 B', 'C': '🟢 C'}
    for haste in ['A', 'B', 'C']:
        cabecalho += f"{hastes_nomes[haste]}".center(espaco_por_haste)
    print(cabecalho + "  ║")
    
    print("╠" + "─" * largura_total + "╣")
    
    # Desenhar os discos (de cima para baixo)
    niveis = []
    for i in range(n):
        nivel = []
        for haste in ['A', 'B', 'C']:
            if i < len(hastes[haste]):
                nivel.append(hastes[haste][i])
            else:
                nivel.append(0)
        niveis.append(nivel)
    
    # Imprimir de cima para baixo
    for nivel in reversed(niveis):
        linha = "║  "
        for disco in nivel:
            if disco == 0:
                # Haste vazia
                espaco = " " * largura_disco_max
                linha += espaco.center(espaco_por_haste)
            else:
                disco_str = disco_colorido(disco, tamanho_maximo)
                # Centralizar o disco no espaço da haste
                linha += disco_str.center(espaco_por_haste)
        print(linha + "  ║")
    
    # Desenhar as hastes verticais
    print("╠" + "─" * largura_total + "╣")
    base = "║  "
    for haste in ['A', 'B', 'C']:
        base += "│".center(espaco_por_haste)
    print(base + "  ║")
    
    # Base inferior
    print("╠" + "═" * largura_total + "╣")
    
    # Estatísticas
    progresso = len(hastes['C']) / n * 100
    tempo_decorrido = int(time.time() - start_time)
    minutos = tempo_decorrido // 60
    segundos = tempo_decorrido % 60
    
    # Eficiência
    if movimentos > 0:
        eficiencia = (minimo_teorico / movimentos) * 100
        if eficiencia > 100:
            eficiencia = 100
    else:
        eficiencia = 0
    
    # Linha de estatísticas
    print(f"║ 📦 Movimentos: {movimentos:<3}  🎯 Mínimo: {minimo_teorico:<3}  📊 Progresso: {progresso:.0f}%".ljust(largura_total) + "║")
    
    # Barra de progresso visual
    barras = int(progresso / 100 * 50)
    barra_progresso = "█" * barras + "░" * (50 - barras)
    print(f"║ [{barra_progresso}] {progresso:.0f}%".ljust(largura_total) + "║")
    
    # Tempo e eficiência
    print(f"║ 💯 Eficiência: {eficiencia:.0f}%  ⏱️  Tempo: {minutos:02d}:{segundos:02d}".ljust(largura_total) + "║")
    
    # Dica inteligente
    dica = gerar_dica_premium(hastes, n)
    # Ajustar dica para caber na largura
    if len(dica) > largura_total - 10:
        dica = dica[:largura_total - 13] + "..."
    print(f"║ 💡 Dica: {dica}".ljust(largura_total) + "║")
    
    print("╠" + "═" * largura_total + "╣")
    
    # Rodapé com controles
    print(f"║ Comandos: A/B/C (ex: A C) | Q para desistir".ljust(largura_total) + "║")
    print("╚" + "═" * largura_total + "╝")

def gerar_dica_premium(hastes, n):
    """Gera dica contextual inteligente"""
    if len(hastes['C']) == n:
        return "🎉 VOCÊ ESTÁ QUASE VENCENDO! Último movimento!"
    elif len(hastes['A']) == n:
        return f"Mova o disco 1 para uma haste vazia (B ou C) - são {n} discos no total"
    elif len(hastes['C']) == n - 1:
        return "Ótimo! Agora mova os discos menores para C"
    elif hastes['B'] and hastes['B'][-1] == 1:
        return "Disco 1 está em B. Use-o como base para outros discos"
    elif hastes['A'] and hastes['A'][-1] == n:
        return f"Libere o disco {n} (o maior) movendo os menores para outra haste"
    elif not hastes['B'] and not hastes['C']:
        return f"Primeiro movimento: leve o disco 1 para B ou C (total de {n} discos)"
    else:
        # Verificar qual haste está vazia
        vazias = [h for h in ['A', 'B', 'C'] if not hastes[h]]
        if vazias:
            return f"Haste {vazias[0]} está vazia. Útil para movimentos estratégicos com {n} discos"
        return "Continue! Observe qual disco pode ser movido"

def animar_movimento_premium(origem, destino, disco):
    """Animação sofisticada de movimento"""
    frames = ["   ╭───╮   ", "   ╭───╮   ", "   ╭───╮   ", "   ╰───╯   ", "       ╭───╮"]
    setas = ["  ↑  ", "  ↗  ", "  →  ", "  ↘  ", "  ↓  "]
    
    print(f"\n Movendo disco {disco}: ", end="", flush=True)
    for i in range(5):
        print(f"\r Movendo disco {disco}: {setas[i]} {frames[i]}", end="", flush=True)
        time.sleep(0.08)
    print(f"\r ✅ Disco {disco} movido: {origem} → {destino}  ")

def movimento_valido_premium(hastes, origem, destino):
    """Verifica se o movimento é permitido"""
    if not hastes[origem]:
        print("\n❌ ERRO: Haste de origem está vazia!")
        return False
    
    disco_origem = hastes[origem][-1]
    
    if hastes[destino]:
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:
            print("\n❌ ERRO: Não pode colocar um disco maior sobre um menor!")
            return False
    
    return True

def mostrar_legenda_premium(n):
    """Mostra legenda colorida dos discos (agora até 8)"""
    print("\n╔" + "═" * 60 + "╗")
    print("║" + " 📖 LEGENDA DOS DISCOS (até 8 cores) ".center(60) + "║")
    print("╠" + "═" * 60 + "╣")
    for i in range(1, n+1):
        disco_str = disco_colorido(i, n)
        print(f"║ Disco {i}: {disco_str}".ljust(61) + "║")
    print("╚" + "═" * 60 + "╝")
    print()

def jogar_hanoi_premium():
    """Função principal do jogo premium (agora suporta 8 discos)"""
    
    print("\n" + "═" * 88)
    print("🎮 BEM-VINDO À TORRE DE HANÓI - EDIÇÃO PREMIUM (8 DISCOS) 🎮".center(88))
    print("═" * 88)
    
    try:
        # Alterado: máximo de 8 discos
        n = int(input("\n🔢 Digite o número de discos (1-8 para melhor visualização): "))
        if n < 1 or n > 8:
            print("Por favor, digite um número entre 1 e 8")
            return
        
        # Inicializar jogo
        hastes = {
            'A': list(range(n, 0, -1)),
            'B': [],
            'C': []
        }
        
        movimentos = 0
        minimo_teorico = 2**n - 1
        start_time = time.time()
        
        # Mostrar legenda
        mostrar_legenda_premium(n)
        
        input("⚡ Pressione ENTER para começar...")
        limpar_tela()
        
        while hastes['C'] != list(range(n, 0, -1)):
            exibir_hastes_premium(hastes, n, movimentos, minimo_teorico, start_time)
            
            # Input do usuário
            print()
            comando = input("🎮 Digite a haste de origem e destino (ex: A C) ou Q para sair: ").upper().strip()
            
            if comando == 'Q':
                print("\n👋 Jogo encerrado! Até a próxima!")
                return
            
            try:
                partes = comando.split()
                if len(partes) != 2:
                    print("\n❌ Formato inválido! Use: ORIGEM DESTINO (ex: A C)")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
                
                origem, destino = partes[0], partes[1]
                
                if origem not in ['A', 'B', 'C'] or destino not in ['A', 'B', 'C']:
                    print("\n❌ Hastes devem ser A, B ou C!")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
                
                if origem == destino:
                    print("\n❌ Origem e destino não podem ser iguais!")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
                
                if movimento_valido_premium(hastes, origem, destino):
                    disco = hastes[origem].pop()
                    hastes[destino].append(disco)
                    movimentos += 1
                    
                    # Animar movimento
                    animar_movimento_premium(origem, destino, disco)
                    time.sleep(0.5)
                    limpar_tela()
                else:
                    time.sleep(1.5)
                    limpar_tela()
                    
            except (ValueError, IndexError):
                print("\n❌ Comando inválido! Use: A C (origem e destino separados por espaço)")
                time.sleep(1.5)
                limpar_tela()
        
        # VITÓRIA!
        limpar_tela()
        exibir_hastes_premium(hastes, n, movimentos, minimo_teorico, start_time)
        
        print("\n" + "🎉" * 44)
        print("🏆 PARABÉNS! VOCÊ VENCEU A TORRE DE HANÓI! 🏆".center(88))
        print("🎉" * 44)
        
        tempo_total = int(time.time() - start_time)
        minutos = tempo_total // 60
        segundos = tempo_total % 60
        
        print(f"\n📊 RESUMO FINAL:")
        print(f"   • Número de discos: {n}")
        print(f"   • Movimentos realizados: {movimentos}")
        print(f"   • Movimentos mínimos: {minimo_teorico}")
        print(f"   • Eficiência: {(minimo_teorico/movimentos*100):.1f}%")
        print(f"   • Tempo total: {minutos:02d}:{segundos:02d}")
        
        # Avaliação final
        if movimentos == minimo_teorico:
            print("\n⭐ PERFEITO! SOLUÇÃO ÓTIMA! Você é um mestre! ⭐")
        elif movimentos <= minimo_teorico * 1.3:
            print("\n🌟 EXCELENTE! Muito eficiente! 🌟")
        elif movimentos <= minimo_teorico * 1.6:
            print("\n👍 BOM! Mas pode melhorar! 👍")
        else:
            print("\n💪 BOA TENTATIVA! Tente novamente para melhorar! 💪")
        
        print("\n" + "═" * 88)
        input("Pressione ENTER para sair...")
        
    except ValueError:
        print("\n❌ Por favor, digite um número válido!")

if __name__ == "__main__":
    jogar_hanoi_premium()
