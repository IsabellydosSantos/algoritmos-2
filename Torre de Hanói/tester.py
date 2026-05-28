#pip install rich
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
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def disco_colorido(numero, tamanho_maximo):
    """Retorna disco colorido com tamanho proporcional"""
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

def exibir_hastes_rich(hastes, n, movimentos, minimo_teorico, start_time):
    """Exibe o jogo usando Rich - SEM PREOCUPAÇÃO COM ALINHAMENTO!"""
    
    # Cria uma tabela com 3 colunas
    table = Table(show_header=True, header_style="bold cyan", box=box.ROUNDED)
    table.add_column("🔴 A", justify="center", width=20)
    table.add_column("🟡 B", justify="center", width=20)
    table.add_column("🟢 C", justify="center", width=20)
    
    # Prepara os discos para exibição
    max_height = n
    niveis = []
    for i in range(max_height):
        nivel = []
        for haste in ['A', 'B', 'C']:
            if i < len(hastes[haste]):
                nivel.append(hastes[haste][i])
            else:
                nivel.append(0)
        niveis.append(nivel)
    
    # Adiciona as linhas da tabela (de cima para baixo)
    for nivel in reversed(niveis):
        row = []
        for disco in nivel:
            if disco == 0:
                row.append("│")
            else:
                row.append(disco_colorido(disco, n))
        table.add_row(*row)
    
    # Adiciona a base
    table.add_row("┴", "┴", "┴")
    
    # Exibe a tabela em um painel
    console.print(Panel(table, title="🎮 Torre de Hanói", border_style="green"))
    
    # Estatísticas
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
    
    # Painel de estatísticas
    stats = f"""
📦 Movimentos: {movimentos}    🎯 Mínimo: {minimo_teorico}    📊 Progresso: {progresso:.0f}%
💯 Eficiência: {eficiencia:.0f}%    ⏱️  Tempo: {minutos:02d}:{segundos:02d}
    """
    console.print(Panel(stats.strip(), border_style="blue"))
    
    # Dica
    dica = gerar_dica_premium(hastes, n)
    console.print(Panel(f"💡 {dica}", border_style="yellow"))

def gerar_dica_premium(hastes, n):
    """Gera dica contextual inteligente"""
    if len(hastes['C']) == n:
        return "🎉 VOCÊ ESTÁ QUASE VENCENDO! Último movimento!"
    elif len(hastes['A']) == n:
        return f"Mova o disco 1 para uma haste vazia (B ou C) - são {n} discos"
    elif len(hastes['C']) == n - 1:
        return "Ótimo! Agora mova os discos menores para C"
    elif hastes['B'] and hastes['B'][-1] == 1:
        return "Disco 1 está em B. Use-o como base para outros discos"
    elif hastes['A'] and hastes['A'][-1] == n:
        return f"Libere o disco {n} (o maior) movendo os menores"
    elif not hastes['B'] and not hastes['C']:
        return f"Primeiro movimento: leve o disco 1 para B ou C"
    else:
        vazias = [h for h in ['A', 'B', 'C'] if not hastes[h]]
        if vazias:
            return f"Haste {vazias[0]} está vazia. Use para movimentos estratégicos"
        return "Continue! Observe qual disco pode ser movido"

def animar_movimento_premium(origem, destino, disco):
    """Animação simplificada de movimento"""
    print(f"\n ✅ Movendo disco {disco}: {origem} → {destino}")
    time.sleep(0.3)

def movimento_valido_premium(hastes, origem, destino):
    """Verifica se o movimento é permitido"""
    if not hastes[origem]:
        console.print("\n❌ ERRO: Haste de origem está vazia!", style="red")
        return False
    
    disco_origem = hastes[origem][-1]
    
    if hastes[destino]:
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:
            console.print("\n❌ ERRO: Não pode colocar um disco maior sobre um menor!", style="red")
            return False
    
    return True

def mostrar_legenda_premium(n):
    """Mostra legenda colorida dos discos"""
    table = Table(title="📖 LEGENDA DOS DISCOS", box=box.ROUNDED)
    table.add_column("Disco", style="cyan", justify="center")
    table.add_column("Cor", justify="center")
    
    for i in range(1, n+1):
        disco_str = disco_colorido(i, n)
        table.add_row(str(i), disco_str)
    
    console.print(table)

def jogar_hanoi_premium():
    """Função principal do jogo"""
    
    console.print("\n[bold yellow]🎮 BEM-VINDO À TORRE DE HANÓI - EDIÇÃO PREMIUM 🎮[/bold yellow]")
    console.print("=" * 60, style="dim")
    
    try:
        n = int(input("\n🔢 Digite o número de discos (1-8): "))
        if n < 1 or n > 8:
            console.print("[red]Por favor, digite um número entre 1 e 8[/red]")
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
        
        input("\n⚡ Pressione ENTER para começar...")
        limpar_tela()
        
        while hastes['C'] != list(range(n, 0, -1)):
            exibir_hastes_rich(hastes, n, movimentos, minimo_teorico, start_time)
            
            # Input do usuário
            print()
            comando = input("🎮 Digite origem e destino (ex: A C) ou Q: ").upper().strip()
            
            if comando == 'Q':
                console.print("\n[red]👋 Jogo encerrado![/red]")
                return
            
            try:
                partes = comando.split()
                if len(partes) != 2:
                    console.print("\n[red]❌ Use: ORIGEM DESTINO (ex: A C)[/red]")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
                
                origem, destino = partes[0], partes[1]
                
                if origem not in ['A', 'B', 'C'] or destino not in ['A', 'B', 'C']:
                    console.print("\n[red]❌ Use A, B ou C![/red]")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
                
                if origem == destino:
                    console.print("\n[red]❌ Hastes diferentes![/red]")
                    time.sleep(1.5)
                    limpar_tela()
                    continue
                
                if movimento_valido_premium(hastes, origem, destino):
                    disco = hastes[origem].pop()
                    hastes[destino].append(disco)
                    movimentos += 1
                    
                    animar_movimento_premium(origem, destino, disco)
                    time.sleep(0.5)
                    limpar_tela()
                else:
                    time.sleep(1.5)
                    limpar_tela()
                    
            except (ValueError, IndexError):
                console.print("\n[red]❌ Comando inválido![/red]")
                time.sleep(1.5)
                limpar_tela()
        
        # VITÓRIA!
        limpar_tela()
        exibir_hastes_rich(hastes, n, movimentos, minimo_teorico, start_time)
        
        console.print("\n[bold green]🎉" * 20 + "[/bold green]")
        console.print("[bold yellow]🏆 PARABÉNS! VOCÊ VENCEU! 🏆[/bold yellow]")
        console.print("[bold green]🎉" * 20 + "[/bold green]")
        
        tempo_total = int(time.time() - start_time)
        minutos = tempo_total // 60
        segundos = tempo_total % 60
        
        console.print("\n[bold]📊 RESUMO FINAL:[/bold]")
        console.print(f"   • Discos: {n}")
        console.print(f"   • Movimentos: {movimentos}")
        console.print(f"   • Mínimo teórico: {minimo_teorico}")
        console.print(f"   • Eficiência: {(minimo_teorico/movimentos*100):.1f}%")
        console.print(f"   • Tempo: {minutos:02d}:{segundos:02d}")
        
        if movimentos == minimo_teorico:
            console.print("\n[bold green]⭐ PERFEITO! SOLUÇÃO ÓTIMA! ⭐[/bold green]")
        elif movimentos <= minimo_teorico * 1.3:
            console.print("\n[bold cyan]🌟 EXCELENTE! 🌟[/bold cyan]")
        elif movimentos <= minimo_teorico * 1.6:
            console.print("\n[bold yellow]👍 BOM! 👍[/bold yellow]")
        else:
            console.print("\n[bold magenta]💪 BOA TENTATIVA! 💪[/bold magenta]")
        
        input("\nPressione ENTER para sair...")
        
    except ValueError:
        console.print("\n[red]❌ Digite um número válido![/red]")

if __name__ == "__main__":
    jogar_hanoi_premium()
