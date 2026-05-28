import time
import os
from prettytable import PrettyTable

# Cores arco-íris (mesmas)
CORES_ARCO_IRIS = {
    1: '\033[91m', 2: '\033[38;5;208m', 3: '\033[93m', 4: '\033[92m',
    5: '\033[94m', 6: '\033[96m', 7: '\033[95m', 8: '\033[38;5;201m'
}
RESET = '\033[0m'

def disco_colorido(numero, tamanho_maximo):
    tamanho = numero * 2 - 1
    cor = CORES_ARCO_IRIS.get(numero, '\033[97m')
    
    if tamanho >= 3:
        disco = "█" * tamanho
        pos = tamanho // 2
        if tamanho > 9:
            disco = disco[:pos-1] + str(numero) + disco[pos:]
        else:
            disco = disco[:pos] + str(numero) + disco[pos+1:]
    else:
        disco = "█" * tamanho
    
    return cor + disco + RESET

def exibir_hastes_prettytable(hastes, n):
    """Exibe usando PrettyTable"""
    table = PrettyTable()
    table.field_names = ["Haste A", "Haste B", "Haste C"]
    table.align = "c"
    table.horizontal_char = "─"
    table.vertical_char = "│"
    table.junction_char = "┼"
    
    max_altura = n
    
    for nivel in range(max_altura - 1, -1, -1):
        linha = []
        for haste in ['A', 'B', 'C']:
            if nivel < len(hastes[haste]):
                disco = hastes[haste][nivel]
                linha.append(disco_colorido(disco, n))
            else:
                linha.append("|")
        table.add_row(linha)
    
    # Linha da base
    table.add_row(["═" * (n * 2 - 1), "═" * (n * 2 - 1), "═" * (n * 2 - 1)])
    
    print(table)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_jogo_pretty(hastes, n, movimentos, minimo_teorico, start_time):
    limpar_tela()
    
    print("=" * 70)
    print(f"{'TORRE DE HANÓI - ' + str(n) + ' DISCOS':^70}")
    print("=" * 70)
    
    progresso = len(hastes['C']) / n * 100
    tempo_decorrido = int(time.time() - start_time)
    minutos = tempo_decorrido // 60
    segundos = tempo_decorrido % 60
    
    if movimentos > 0:
        eficiencia = (minimo_teorico / movimentos) * 100
        if eficiencia > 100:
            eficiencia = 100
    else:
        eficiencia = 0
    
    # Tabela de estatísticas
    stats = PrettyTable()
    stats.field_names = ["Métrica", "Valor"]
    stats.align = "l"
    stats.add_row(["📦 Movimentos", movimentos])
    stats.add_row(["🎯 Mínimo", minimo_teorico])
    stats.add_row(["📊 Progresso", f"{progresso:.0f}%"])
    stats.add_row(["💯 Eficiência", f"{eficiencia:.0f}%"])
    stats.add_row(["⏱️  Tempo", f"{minutos:02d}:{segundos:02d}"])
    print(stats)
    
    print()
    barras = int(progresso / 100 * 40)
    print(f"[{'█' * barras}{'░' * (40 - barras)}] {progresso:.0f}%")
    print()
    
    exibir_hastes_prettytable(hastes, n)
    
    print(f"\n💡 Dica: {gerar_dica(hastes, n)}")
    print("\nComandos: A B (origem e destino) | Q")

def gerar_dica(hastes, n):
    if len(hastes['C']) == n:
        return "🎉 Último movimento!"
    elif len(hastes['A']) == n:
        return f"Mova disco 1 para B ou C"
    else:
        return "Disco menor sobre maior"

def mostrar_legenda_pretty(n):
    print("\n📖 LEGENDA DOS DISCOS")
    legenda = PrettyTable()
    legenda.field_names = ["Disco", "Visual"]
    legenda.align = "l"
    for i in range(1, n+1):
        legenda.add_row([f"Disco {i}", disco_colorido(i, n)])
    print(legenda)

def movimento_valido(hastes, origem, destino):
    if not hastes[origem]:
        print("\n❌ Haste origem vazia!")
        return False
    disco_origem = hastes[origem][-1]
    if hastes[destino] and disco_origem > hastes[destino][-1]:
        print("\n❌ Disco maior sobre menor!")
        return False
    return True

def jogar_hanoi_pretty():
    print("=" * 70)
    print("🎮 TORRE DE HANÓI - EDIÇÃO PRETTYTABLE 🎮")
    print("=" * 70)
    
    try:
        n = int(input("\n🔢 Discos (1-8): "))
        if n < 1 or n > 8:
            print("Digite 1-8")
            return
        
        hastes = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
        movimentos = 0
        minimo_teorico = 2**n - 1
        start_time = time.time()
        
        mostrar_legenda_pretty(n)
        input("\nPressione ENTER...")
        
        while hastes['C'] != list(range(n, 0, -1)):
            exibir_jogo_pretty(hastes, n, movimentos, minimo_teorico, start_time)
            
            comando = input("\n> ").upper().strip()
            if comando == 'Q':
                print("Saindo...")
                return
            
            try:
                if len(comando.split()) != 2:
                    print("Use: ORIGEM DESTINO")
                    time.sleep(1)
                    continue
                
                origem, destino = comando.split()
                if origem not in 'ABC' or destino not in 'ABC':
                    print("Use A, B, C")
                    time.sleep(1)
                    continue
                
                if movimento_valido(hastes, origem, destino):
                    disco = hastes[origem].pop()
                    hastes[destino].append(disco)
                    movimentos += 1
                    print(f"\n✅ {origem} → {destino} (Disco {disco})")
                    time.sleep(0.3)
                    
            except:
                print("Inválido!")
                time.sleep(1)
        
        exibir_jogo_pretty(hastes, n, movimentos, minimo_teorico, start_time)
        print("\n🏆 PARABÉNS! 🏆")
        
    except ValueError:
        print("Número inválido!")

if __name__ == "__main__":
    jogar_hanoi_pretty()
