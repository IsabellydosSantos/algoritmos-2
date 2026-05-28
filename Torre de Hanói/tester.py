import time
import os
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, BarColumn
from rich.text import Text
from rich.align import Align

# Códigos de cor ANSI para os discos (arco-íris)
CORES_ARCO_IRIS = {
    1: '\033[91m',   # Vermelho
    2: '\033[38;5;208m', # Laranja
    3: '\033[93m',   # Amarelo
    4: '\033[92m',   # Verde
    5: '\033[94m',   # Azul
    6: '\033[96m',   # Anil/Ciano
    7: '\033[95m',   # Violeta/Roxo
    8: '\033[38;5;201m', # Magenta/Rosa
}
RESET = '\033[0m'

console = Console()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def disco_colorido(numero, tamanho_maximo):
    """Retorna disco colorido com tamanho proporcional"""
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

def desenhar_hastes_rich(hastes, n):
    """Desenha as hastes usando Rich Table"""
    tamanho_maximo = n
    largura_haste = tamanho_maximo * 2 + 2
    
    # Criar tabela para as hastes
    table = Table(show_header=True, header_style="bold white", show_edge=False, padding=(0, 2))
    table.add_column("Haste A", justify="center", width=largura_haste)
    table.add_column("Haste B", justify="center", width=largura_haste)
    table.add_column("Haste C", justify="center", width=largura_haste)
    
    # Encontrar altura máxima
    max_altura = n
    
    # Construir linhas de cima para baixo
    for nivel in range(max_altura - 1, -1, -1):
        linha_a = ""
        linha_b = ""
        linha_c = ""
        
        # Haste A
        if nivel < len(hastes['A']):
            disco = hastes['A'][nivel]
            disco_str = disco_colorido(disco, n)
            linha_a = disco_str.center(largura_haste)
        else:
            linha_a = "|".center(largura_haste)
        
        # Haste B
        if nivel < len(hastes['B']):
            disco = hastes['B'][nivel]
            disco_str = disco_colorido(disco, n)
            linha_b = disco_str.center(largura_haste)
        else:
            linha_b = "|".center(largura_haste)
        
        # Haste C
        if nivel < len(hastes['C']):
            disco = hastes['C'][nivel]
            disco_str = disco_colorido(disco, n)
            linha_c = disco_str.center(largura_haste)
        else:
            linha_c = "|".center(largura_haste)
        
        table.add_row(linha_a, linha_b, linha_c)
    
    # Adicionar linha da base
    base_a = "═" * (largura_haste - 2)
    table.add_row(f" {base_a} ", f" {base_a} ", f" {base_a} ")
    
    return table

def exibir_jogo_rich(hastes, n, movimentos, minimo_teorico, start_time):
    """Exibição completa usando Rich"""
    console.clear()
    
    # Título
    console.print(Panel(Align.center(f"[bold cyan]TORRE DE HANÓI - {n} DISCOS[/bold cyan]"), 
                        border_style="cyan"))
    
    # Estatísticas em grid
    stats_table = Table(show_header=False, show_edge=False, box=None)
    stats_table.add_column(justify="left", width=20)
    stats_table.add_column(justify="left", width=20)
    stats_table.add_column(justify="left", width=20)
    
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
    
    stats_table.add_row(f"📦 Movimentos: {movimentos}", 
                        f"🎯 Mínimo: {minimo_teorico}", 
                        f"📊 Progresso: {progresso:.0f}%")
    stats_table.add_row(f"💯 Eficiência: {eficiencia:.0f}%", 
                        f"⏱️  Tempo: {minutos:02d}:{segundos:02d}", 
                        f"{'█' * int(progresso/2)}{'░' * (50 - int(progresso/2))}")
    
    console.print(stats_table)
    console.print()
    
    # Desenhar hastes
    console.print(desenhar_hastes_rich(hastes, n))
    
    # Dica
    dica = gerar_dica_premium(hastes, n)
    console.print(Panel(dica, border_style="yellow", title="💡 Dica"))
    
    # Comandos
    console.print("[dim]Comandos: A/B/C para haste de origem e destino (ex: A B) | Q para desistir[/dim]")

def gerar_dica_premium(hastes, n):
    """Gera dica contextual"""
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
        vazias = [h for h in ['A', 'B', 'C'] if not hastes[h]]
        if vazias:
            return f"Haste {vazias[0]} está vazia. Útil para movimentos estratégicos com {n} discos"
        return "Continue! Observe qual disco pode ser movido"

def mostrar_legenda_rich(n):
    """Mostra legenda colorida dos discos"""
    console.print("\n[bold]📖 LEGENDA DOS DISCOS (Arco-Íris)[/bold]")
    legenda_table = Table(show_header=False, show_edge=False)
    legenda_table.add_column(justify="left", width=15)
    legenda_table.add_column(justify="left", width=30)
    
    for i in range(1, n+1):
        disco_str = disco_colorido(i, n)
        cores = {1:"Vermelho", 2:"Laranja", 3:"Amarelo", 4:"Verde", 
                 5:"Azul", 6:"Anil", 7:"Violeta", 8:"Magenta"}
        legenda_table.add_row(f"Disco {i}:", f"{disco_str} ({cores[i]})")
    
    console.print(legenda_table)

def movimento_valido(hastes, origem, destino):
    """Verifica se o movimento é permitido"""
    if not hastes[origem]:
        console.print("\n[red]❌ ERRO: Haste de origem está vazia![/red]")
        return False
    
    disco_origem = hastes[origem][-1]
    
    if hastes[destino]:
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:
            console.print("\n[red]❌ ERRO: Não pode colocar um disco maior sobre um menor![/red]")
            return False
    
    return True

def jogar_hanoi_rich():
    """Função principal com Rich"""
    
    console.print("\n[bold cyan]" + "═" * 60 + "[/bold cyan]")
    console.print(Align.center("[bold yellow]🎮 TORRE DE HANÓI - EDIÇÃO RICH 🎮[/bold yellow]"))
    console.print("[bold cyan]" + "═" * 60 + "[/bold cyan]")
    
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
        mostrar_legenda_rich(n)
        
        input("\n⚡ Pressione ENTER para começar...")
        
        while hastes['C'] != list(range(n, 0, -1)):
            exibir_jogo_rich(hastes, n, movimentos, minimo_teorico, start_time)
            
            comando = input("\n🎮 Comando (ex: A B) ou Q: ").upper().strip()
            
            if comando == 'Q':
                console.print("\n[yellow]👋 Jogo encerrado! Até a próxima![/yellow]")
                return
            
            try:
                partes = comando.split()
                if len(partes) != 2:
                    console.print("[red]❌ Formato inválido! Use: ORIGEM DESTINO (ex: A C)[/red]")
                    time.sleep(1.5)
                    continue
                
                origem, destino = partes[0], partes[1]
                
                if origem not in ['A', 'B', 'C'] or destino not in ['A', 'B', 'C']:
                    console.print("[red]❌ Hastes devem ser A, B ou C![/red]")
                    time.sleep(1.5)
                    continue
                
                if origem == destino:
                    console.print("[red]❌ Origem e destino não podem ser iguais![/red]")
                    time.sleep(1.5)
                    continue
                
                if movimento_valido(hastes, origem, destino):
                    disco = hastes[origem].pop()
                    hastes[destino].append(disco)
                    movimentos += 1
                    
                    # Efeito visual
                    console.print(f"\n[green]✅ Disco {disco} movido: {origem} → {destino}[/green]")
                    time.sleep(0.3)
                    
            except (ValueError, IndexError):
                console.print("[red]❌ Comando inválido![/red]")
                time.sleep(1.5)
        
        # VITÓRIA!
        exibir_jogo_rich(hastes, n, movimentos, minimo_teorico, start_time)
        
        console.print("\n[bold yellow]" + "🎉" * 30 + "[/bold yellow]")
        console.print(Align.center("[bold green]🏆 PARABÉNS! VOCÊ VENCEU! 🏆[/bold green]"))
        console.print("[bold yellow]" + "🎉" * 30 + "[/bold yellow]")
        
        tempo_total = int(time.time() - start_time)
        minutos = tempo_total // 60
        segundos = tempo_total % 60
        
        console.print(f"\n[bold]📊 RESUMO FINAL:[/bold]")
        console.print(f"   • Número de discos: {n}")
        console.print(f"   • Movimentos realizados: {movimentos}")
        console.print(f"   • Movimentos mínimos: {minimo_teorico}")
        console.print(f"   • Eficiência: {(minimo_teorico/movimentos*100):.1f}%")
        console.print(f"   • Tempo total: {minutos:02d}:{segundos:02d}")
        
        if movimentos == minimo_teorico:
            console.print("\n[bold magenta]⭐ PERFEITO! SOLUÇÃO ÓTIMA! ⭐[/bold magenta]")
        
        input("\nPressione ENTER para sair...")
        
    except ValueError:
        console.print("[red]❌ Por favor, digite um número válido![/red]")

if __name__ == "__main__":
    jogar_hanoi_rich()
