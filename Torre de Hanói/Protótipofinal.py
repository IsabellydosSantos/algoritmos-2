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
            area = [" "] * largura_area  
            centro = largura_area // 2  
            
            if nivel < len(hastes[haste]):  
                disco = hastes[haste][nivel] 
                texto = criar_texto_disco(disco)
                largura_disco = len(texto)
                
                inicio = centro - largura_disco // 2
                cor = CORES.get(disco, '\033[97m') 
                
                for i, char in enumerate(texto):
                    pos = inicio + i
                    if 0 <= pos < largura_area:
                        area[pos] = cor + char + RESET  # Aplica cor
            else:
                area[centro] = "│"
            
            linha += "".join(area)
        
        print(linha)
    
    print("-" * largura_total)
    
    progresso = (len(hastes['C']) / n) * 100 
    
    tempo_decorrido = int(time.time() - start_time)
    minutos = tempo_decorrido // 60
    segundos = tempo_decorrido % 60
    
    print(f"\n📊 Movimentos: {movimentos}  |  ⭐ Mínimo teórico: {minimo_teorico}")
    
    barras = int((progresso / 100) * 40)
    barra = "█" * barras + "░" * (40 - barras)
    print(f"📈 [{barra}] {progresso:.0f}%")
    
    print(f"⏱ Tempo: {minutos:02d}:{segundos:02d}")
    print("\nComandos: A C | DICA | Q")
    print("=" * largura_total)


def movimento_valido(hastes, origem, destino):
    if not hastes[origem]:
        print("\n❌ Haste vazia!")
        return False
    
    disco_origem = hastes[origem][-1] 
    
    if hastes[destino]:
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:
            print("\n❌ Disco maior sobre menor!")
            return False
    
    return True


def animar_movimento(origem, destino, disco):
    print(f"\n➡️ Disco {disco}: {origem} → {destino}")
    time.sleep(0.3)  


def encontrar_proximo_movimento(hastes, n, origem, destino, auxiliar):
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
    if len(hastes['C']) == n:
        return "🎉 Você já venceu!"
    
    proximo = encontrar_proximo_movimento(hastes, n, 'A', 'C', 'B')
    if proximo:
        origem, destino, disco = proximo
        return f"Mova o disco {disco} da haste {origem} para a haste {destino}"
    
    return "Digite um comando válido."


def jogar_hanoi():    
    print("\n" + "=" * 50)
    print("TORRE DE HANÓI".center(50))
    print("=" * 50)
    
    try:
        n = int(input("\nNúmero de discos (1-8): "))
        
        if n < 1 or n > 8:
            print("Digite um número entre 1 e 8.")
            return
        
        hastes = {
            'A': list(range(n, 0, -1)), 
            'B': [],
            'C': []
        }
        
        movimentos = 0
        minimo_teorico = (2 ** n - 1)  
        start_time = time.time() 
        
        while hastes['C'] != list(range(n, 0, -1)):
            exibir_hastes(hastes, n, movimentos, minimo_teorico, start_time)
            
            comando = input("\n🎮 Jogada (A C), DICA ou Q: ").upper().strip()
            
            if comando == 'Q':
                print("\n👋 Até logo!")
                return
            
            if comando == 'DICA':
                dica = gerar_dica_solucao(hastes, n)
                print(f"\n💡 {dica}")
                input("\nENTER para continuar...")
                continue
            
            partes = comando.split()
            if len(partes) != 2:
                print("\n❌ Use: A C")
                time.sleep(1)
                continue
            
            origem, destino = partes
            
            if origem not in ['A', 'B', 'C'] or destino not in ['A', 'B', 'C']:
                print("\n❌ Haste inválida")
                time.sleep(1)
                continue
            
            if origem == destino:
                print("\n❌ Iguais")
                time.sleep(1)
                continue
            
            if movimento_valido(hastes, origem, destino):
                disco = hastes[origem].pop()  # Remove da origem
                hastes[destino].append(disco)  # Adiciona ao destino
                movimentos += 1
                animar_movimento(origem, destino, disco)
        
        exibir_hastes(hastes, n, movimentos, minimo_teorico, start_time)
        print("\n🎉 Parabéns! 🎉\n")
        
        tempo_total = int(time.time() - start_time)
        minutos = tempo_total // 60
        segundos = tempo_total % 60
        
        print(f"Discos: {n}")
        print(f"Movimentos: {movimentos}")
        print(f"Tempo: {minutos:02d}:{segundos:02d}")
        
        if movimentos == minimo_teorico:
            print("\n⭐ Solução perfeita! ⭐")
        
        input("\nENTER para sair...")
    
    except ValueError:
        print("\nDigite um número válido.")


if __name__ == "__main__":
    jogar_hanoi()  # Só executa se o arquivo for rodado diretamente
