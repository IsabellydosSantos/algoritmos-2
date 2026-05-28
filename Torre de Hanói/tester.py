#pip install rich
⚡ Pressione ENTER para começar...
┌───────────────────────────── 🎮 TORRE DE HANÓI ─────────────────────────────┐
│                                                                             │
│  ┌───────────────────────┬───────────────────────┬───────────────────────┐  │
│  │      🔴 HASTE A       │      🟡 HASTE B       │      🟢 HASTE C       │  │
│  ├───────────────────────┼───────────────────────┼───────────────────────┤  │
│  │       █        │                       │                       │  │
│  │      █2█       │                       │                       │  │
│  │     ██3██      │                       │                       │  │
│  │         ━━━━━         │         ━━━━━         │         ━━━━━         │  │
│  └───────────────────────┴───────────────────────┴───────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
┌────────────────────────────── 📊 ESTATÍSTICAS ──────────────────────────────┐
│                                                                             │
│   📦 Movimentos:       0                                                    │
│   🎯 Mínimo teórico:   7                                                    │
│   📊 Progresso:        0%                                                   │
│   💯 Eficiência:       0%                                                   │
│   ⏱️  Tempo:           00:01                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
┌────────────────────────────────── 💡 DICA ──────────────────────────────────┐
│ Mova o disco 1 para uma haste vazia (B ou C)                                │
└─────────────────────────────────────────────────────────────────────────────┘

🎮 Origem e destino (ex: A C) ou Q: 
import time
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

# Códigos de cor ANSI
CORES = {
    1: '\033[91m',  # Vermelho
    2: '\033[93m',  # Amarelo
    3: '\033[92m',  # Verde
    4: '\033[94m',  # Azul
    5: '\033[95m',  # Roxo
    6: '\033[96m',  # Ciano
    7: '\033[97m',  # Branco
    8: '\033[90m',  # Cinza
}
RESET = '\033[0m'

console = Console()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def disco_colorido(numero, tamanho_maximo):
    tamanho = numero * 2 - 1
    cor = CORES.get(numero, '\033[97m')
    
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

def exibir_jogo(hastes, n, movimentos, minimo_teorico, start_time):
    """Exibe o jogo com moldura perfeita usando Rich"""
    
    # Tabela principal
    table = Table(show_header=True, header_style="bold cyan", box=box.ROUNDED)
    table.add_column("🔴 HASTE A", justify="center", width=22)
    table.add_column("🟡 HASTE B", justify="center", width=22)
    table.add_column("🟢 HASTE C", justify="center", width=22)
    
    # Prepara os níveis
    niveis = []
    for i in range(n):
        nivel = []
        for haste in ['A', 'B', 'C']:
            if i < len(hastes[haste]):
                nivel.append(hastes[haste][i])
            else:
                nivel.append(0)
        niveis.append(nivel)
    
    # Adiciona linhas (do topo para baixo)
    for nivel in reversed(niveis):
        linha = []
        for disco in nivel:
            if disco == 0:
                linha.append(" " * (n * 2 - 1))
            else:
                linha.append(disco_colorido(disco, n))
        table.add_row(*linha)
    
    # Base
    table.add_row("━" * (n * 2 - 1), "━" * (n * 2 - 1), "━" * (n * 2 - 1))
    
    # Exibe o jogo
    console.print(Panel(table, title="🎮 TORRE DE HANÓI", border_style="green", padding=(1, 2)))
    
    # Estatísticas
    progresso = len(hastes['C']) / n * 100
    tempo = int(time.time() - start_time)
    minutos = tempo // 60
    segundos = tempo % 60
    
    if movimentos > 0:
        eficiencia = min(100, (minimo_teorico / movimentos) * 100)
    else:
        eficiencia = 0
    
    # Painel de estatísticas
    stats = Table(show_header=False, box=box.SIMPLE)
    stats.add_row("📦 Movimentos:", f"{movimentos}")
    stats.add_row("🎯 Mínimo teórico:", f"{minimo_teorico}")
    stats.add_row("📊 Progresso:", f"{progresso:.0f}%")
    stats.add_row("💯 Eficiência:", f"{eficiencia:.0f}%")
    stats.add_row("⏱️  Tempo:", f"{minutos:02d}:{segundos:02d}")
    
    console.print(Panel(stats, title="📊 ESTATÍSTICAS", border_style="blue"))
    
    # Dica
    dica = gerar_dica(hastes, n)
    console.print(Panel(dica, title="💡 DICA", border_style="yellow"))

def gerar_dica(hastes, n):
    if len(hastes['C']) == n:
        return "🎉 VOCÊ ESTÁ QUASE VENCENDO! Último movimento!"
    elif len(hastes['A']) == n:
        return f"Mova o disco 1 para uma haste vazia (B ou C)"
    elif len(hastes['C']) == n - 1:
        return "Ótimo! Agora mova os discos menores para C"
    elif hastes['B'] and hastes['B'][-1] == 1:
        return "Disco 1 está em B. Use-o como base"
    elif hastes['A'] and hastes['A'][-1] == n:
        return f"Libere o disco {n} movendo os menores"
    elif not hastes['B'] and not hastes['C']:
        return f"Primeiro movimento: leve o disco 1 para B ou C"
    else:
        vazias = [h for h in ['A', 'B', 'C'] if not hastes[h]]
        if vazias:
            return f"Haste {vazias[0]} está vazia"
        return "Observe qual disco pode ser movido"

def movimento_valido(hastes, origem, destino):
    if not hastes[origem]:
        console.print("\n❌ Haste de origem está vazia!", style="red")
        return False
    
    disco_origem = hastes[origem][-1]
    
    if hastes[destino]:
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:
            console.print("\n❌ Disco maior não pode ficar sobre menor!", style="red")
            return False
    
    return True

def mostrar_legenda(n):
    table = Table(title="📖 LEGENDA DOS DISCOS", box=box.ROUNDED)
    table.add_column("Disco", style="cyan", justify="center")
    table.add_column("Visual", justify="center")
    
    for i in range(1, n+1):
        table.add_row(str(i), disco_colorido(i, n))
    
    console.print(table)

def jogar():
    console.print("\n[bold yellow]🎮 TORRE DE HANÓI - EDIÇÃO PREMIUM[/bold yellow]")
    console.print("=" * 50, style="dim")
    
    try:
        n = int(input("\n🔢 Número de discos (1-8): "))
        if n < 1 or n > 8:
            console.print("[red]Digite 1 a 8![/red]")
            return
        
        hastes = {
            'A': list(range(n, 0, -1)),
            'B': [],
            'C': []
        }
        
        movimentos = 0
        minimo = 2**n - 1
        inicio = time.time()
        
        mostrar_legenda(n)
        input("\n⚡ Pressione ENTER para começar...")
        limpar_tela()
        
        while hastes['C'] != list(range(n, 0, -1)):
            exibir_jogo(hastes, n, movimentos, minimo, inicio)
            
            print()
            comando = input("🎮 Origem e destino (ex: A C) ou Q: ").upper().strip()
            
            if comando == 'Q':
                console.print("\n[red]Jogo encerrado![/red]")
                return
            
            try:
                partes = comando.split()
                if len(partes) != 2:
                    console.print("[red]Use: ORIGEM DESTINO[/red]")
                    time.sleep(1)
                    limpar_tela()
                    continue
                
                origem, destino = partes[0], partes[1]
                
                if origem not in 'ABC' or destino not in 'ABC':
                    console.print("[red]Use A, B ou C![/red]")
                    time.sleep(1)
                    limpar_tela()
                    continue
                
                if origem == destino:
                    console.print("[red]Hastes diferentes![/red]")
                    time.sleep(1)
                    limpar_tela()
                    continue
                
                if movimento_valido(hastes, origem, destino):
                    disco = hastes[origem].pop()
                    hastes[destino].append(disco)
                    movimentos += 1
                    console.print(f"\n[green]✅ Disco {disco} movido: {origem} → {destino}[/green]")
                    time.sleep(0.3)
                    limpar_tela()
                else:
                    time.sleep(1)
                    limpar_tela()
                    
            except:
                console.print("[red]Comando inválido![/red]")
                time.sleep(1)
                limpar_tela()
        
        # Vitória
        limpar_tela()
        exibir_jogo(hastes, n, movimentos, minimo, inicio)
        
        console.print("\n[bold green]🎉" * 15 + "[/bold green]")
        console.print("[bold yellow]🏆 PARABÉNS! VOCÊ VENCEU! 🏆[/bold yellow]")
        console.print("[bold green]🎉" * 15 + "[/bold green]")
        
        tempo_total = int(time.time() - inicio)
        
        console.print("\n[bold]RESUMO:[/bold]")
        console.print(f"   • Discos: {n}")
        console.print(f"   • Movimentos: {movimentos}")
        console.print(f"   • Mínimo: {minimo}")
        console.print(f"   • Eficiência: {(minimo/movimentos*100):.1f}%")
        console.print(f"   • Tempo: {tempo_total//60:02d}:{tempo_total%60:02d}")
        
        input("\nPressione ENTER para sair...")
        
    except ValueError:
        console.print("[red]Digite um número![/red]")

if __name__ == "__main__":
    jogar()
