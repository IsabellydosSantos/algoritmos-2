import time
import os

CORES = {
    1: '\033[91m',   # Vermelho 
    2: '\033[33m',   # "Laranja"
    3: '\033[93m',   # Amarelo claro
    4: '\033[92m',   # Verde
    5: '\033[96m',   # Ciano 
    6: '\033[94m',   # Azul
    7: '\033[95m',   # Roxo 
    8: '\033[35m',   # Magenta (para 8 discos, cor complementar)
}

RESET = '\033[0m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def largura_terminal():
    try:
        return os.get_terminal_size().columns
    except:
        return 80


def criar_texto_disco(numero):
    largura = numero * 2 - 1
    texto = "█" * largura
    
    if largura >= 3:  
        meio = largura // 2
        texto = texto[:meio] + str(numero) + texto[meio + 1:]
    
    return texto


def exibir_hastes(hastes, n, movimentos, minimo_teorico, start_time):
    largura_total = largura_terminal()
    largura_area = largura_total // 3 
    limpar_tela()
    
    print("=" * largura_total)
    print("🎮 TORRE DE HANÓI 🎮".center(largura_total))
    print("=" * largura_total)
    print(f"\nObjetivo: mover {n} discos de A → C\n")
    
    linha_topo = ""
    for letra in ['A', 'B', 'C']:
        linha_topo += letra.center(largura_area)
    print(linha_topo)
    print("-" * largura_total)
    
    for nivel in range(n - 1, -1, -1):
        linha = ""
        
        for haste in ['A', 'B', 'C']:
            area = [" "] * largura_area  # Cria área vazia para esta haste
            centro = largura_area // 2    # Posição central
            
            if nivel < len(hastes[haste]):  # Se existe disco neste nível
                disco = hastes[haste][nivel]  # Pega o número do disco
                texto = criar_texto_disco(disco)  # Cria visual do disco
                largura_disco = len(texto)
                
                # Centraliza o disco na haste
                inicio = centro - largura_disco // 2
                cor = CORES.get(disco, '\033[97m')  # Pega a cor do disco
                
                # Desenha cada caractere do disco na posição correta
                for i, char in enumerate(texto):
                    pos = inicio + i
                    if 0 <= pos < largura_area:
                        area[pos] = cor + char + RESET  # Aplica cor
            else:
                # Sem disco, desenha o suporte "│"
                area[centro] = "│"
            
            linha += "".join(area)
        
        print(linha)
    
    print("-" * largura_total)
    
    # === ESTATÍSTICAS DO JOGO ===
    progresso = (len(hastes['C']) / n) * 100  # Percentual completado
    
    # Calcula tempo decorrido
    tempo_decorrido = int(time.time() - start_time)
    minutos = tempo_decorrido // 60
    segundos = tempo_decorrido % 60
    
    # Exibe movimentos e meta
    print(f"\n📊 Movimentos: {movimentos}  |  ⭐ Mínimo teórico: {minimo_teorico}")
    
    # Barra de progresso (40 blocos)
    barras = int((progresso / 100) * 40)
    barra = "█" * barras + "░" * (40 - barras)
    print(f"📈 [{barra}] {progresso:.0f}%")
    
    # Tempo e comandos
    print(f"⏱ Tempo: {minutos:02d}:{segundos:02d}")
    print("\nComandos: A C | DICA | Q")
    print("=" * largura_total)

# =========================
# VALIDAÇÃO
# =========================

def movimento_valido(hastes, origem, destino):
    """Verifica se o movimento é permitido pelas regras da Torre de Hanói"""
    
    # Regra 1: haste origem não pode estar vazia
    if not hastes[origem]:
        print("\n❌ Haste vazia!")
        return False
    
    disco_origem = hastes[origem][-1]  # Pega disco do topo
    
    # Regra 2: disco maior não pode ficar sobre menor
    if hastes[destino]:
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:
            print("\n❌ Disco maior sobre menor!")
            return False
    
    return True

# =========================
# ANIMAÇÃO
# =========================

def animar_movimento(origem, destino, disco):
    """Mostra uma animação simples do movimento"""
    print(f"\n➡️ Disco {disco}: {origem} → {destino}")
    time.sleep(0.3)  # Pequena pausa para efeito visual

# =========================
# DICAS (ALGORITMO RECURSIVO)
# =========================

def encontrar_proximo_movimento(hastes, n, origem, destino, auxiliar):
    """Usa recursão para encontrar o próximo movimento ótimo"""
    
    # Caso base: mover disco 1 diretamente
    if n == 1:
        if hastes[origem] and hastes[origem][-1] == 1:
            return (origem, destino, 1)
        return None
    
    # Se o disco n está na origem e pode ser movido
    if hastes[origem] and hastes[origem][-1] == n:
        # Verifica se todos os discos menores estão na haste auxiliar
        menores_ok = True
        for i in range(1, n):
            if i not in hastes[auxiliar]:
                menores_ok = False
                break
        
        if menores_ok:
            return (origem, destino, n)
        
        # Senão, move os menores para a auxiliar
        return encontrar_proximo_movimento(hastes, n - 1, origem, auxiliar, destino)
    
    # Procura o disco n em outra haste
    for haste in ['A', 'B', 'C']:
        if hastes[haste] and hastes[haste][-1] == n:
            if haste == origem:
                return encontrar_proximo_movimento(hastes, n - 1, origem, auxiliar, destino)
            else:
                return encontrar_proximo_movimento(hastes, n - 1, haste, destino, origem)
    
    return None

def gerar_dica_solucao(hastes, n):
    """Gera uma dica textual do próximo movimento ideal"""
    
    if len(hastes['C']) == n:
        return "🎉 VOCÊ JÁ VENCEU!"
    
    proximo = encontrar_proximo_movimento(hastes, n, 'A', 'C', 'B')
    if proximo:
        origem, destino, disco = proximo
        return f"Mova o disco {disco} da haste {origem} para a haste {destino}"
    
    return "Digite um comando válido."

# =========================
# JOGO PRINCIPAL
# =========================

def jogar_hanoi():
    """Função principal que gerencia todo o jogo"""
    
    print("\n" + "=" * 50)
    print("TORRE DE HANÓI".center(50))
    print("=" * 50)
    
    try:
        # Configuração inicial
        n = int(input("\nNúmero de discos (1-8): "))
        
        if n < 1 or n > 8:
            print("Digite entre 1 e 8.")
            return
        
        # Estado inicial: todos discos em A, B e C vazios
        hastes = {
            'A': list(range(n, 0, -1)),  # [n, n-1, ..., 1]
            'B': [],
            'C': []
        }
        
        movimentos = 0
        minimo_teorico = (2 ** n - 1)  # Fórmula matemática
        start_time = time.time()  # Marca início
        
        # Loop principal do jogo
        while hastes['C'] != list(range(n, 0, -1)):  # Enquanto não venceu
            exibir_hastes(hastes, n, movimentos, minimo_teorico, start_time)
            
            comando = input("\n🎮 Jogada (A C), DICA ou Q: ").upper().strip()
            
            # Opção sair
            if comando == 'Q':
                print("\n👋 Até logo!")
                return
            
            # Opção dica
            if comando == 'DICA':
                dica = gerar_dica_solucao(hastes, n)
                print(f"\n💡 {dica}")
                input("\nENTER para continuar...")
                continue
            
            # Processa movimento (ex: "A C")
            partes = comando.split()
            if len(partes) != 2:
                print("\n❌ Use: A C")
                time.sleep(1)
                continue
            
            origem, destino = partes
            
            # Valida hastes
            if origem not in ['A', 'B', 'C'] or destino not in ['A', 'B', 'C']:
                print("\n❌ Haste inválida")
                time.sleep(1)
                continue
            
            if origem == destino:
                print("\n❌ Iguais")
                time.sleep(1)
                continue
            
            # Executa movimento se válido
            if movimento_valido(hastes, origem, destino):
                disco = hastes[origem].pop()  # Remove da origem
                hastes[destino].append(disco)  # Adiciona ao destino
                movimentos += 1
                animar_movimento(origem, destino, disco)
        
        # === VITÓRIA ===
        exibir_hastes(hastes, n, movimentos, minimo_teorico, start_time)
        print("\n🎉 PARABÉNS! 🎉\n")
        
        tempo_total = int(time.time() - start_time)
        minutos = tempo_total // 60
        segundos = tempo_total % 60
        
        print(f"Discos: {n}")
        print(f"Movimentos: {movimentos}")
        print(f"Tempo: {minutos:02d}:{segundos:02d}")
        
        if movimentos == minimo_teorico:
            print("\n⭐ SOLUÇÃO PERFEITA! ⭐")
        
        input("\nENTER para sair...")
    
    except ValueError:
        print("\nDigite um número válido.")

# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    jogar_hanoi()  # Só executa se o arquivo for rodado diretamente
