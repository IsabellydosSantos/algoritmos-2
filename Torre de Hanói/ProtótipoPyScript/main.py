from pyscript import document
from js import console, window
import json

# Estado global
movimentos_globais = []
hastes_atuais = None
num_discos_atual = 3

def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        movimento = f"Mover disco 1 de {origem} para {destino}"
        movimentos_globais.append(movimento)
        # Atualizar visualização das hastes
        atualizar_hastes_visual(origem, destino, 1)
        return 1
    
    movimentos = 0
    movimentos += torre_hanoi(n-1, origem, auxiliar, destino)
    
    movimento = f"Mover disco {n} de {origem} para {destino}"
    movimentos_globais.append(movimento)
    # Atualizar visualização das hastes
    atualizar_hastes_visual(origem, destino, n)
    movimentos += 1
    
    movimentos += torre_hanoi(n-1, auxiliar, destino, origem)
    
    return movimentos

def atualizar_hastes_visual(origem, destino, disco):
    """Atualiza a representação visual das hastes"""
    global hastes_atuais
    
    # Remover disco da haste de origem
    hastes_atuais[origem].remove(disco)
    # Adicionar disco à haste de destino
    hastes_atuais[destino].append(disco)
    
    # Ordenar discos (maior na base)
    for haste in hastes_atuais:
        hastes_atuais[haste].sort(reverse=True)
    
    # Desenhar hastes no DOM
    desenhar_hastes()

def desenhar_hastes():
    """Desenha as hastes com os discos atuais no HTML"""
    for haste in ['A', 'B', 'C']:
        discos_container = document.getElementById(f"discos-{haste}")
        discos_container.innerHTML = ""
        
        discos = hastes_atuais.get(haste, [])
        max_disco = num_discos_atual
        min_width = 40
        max_width = 120
        step = (max_width - min_width) / max_disco if max_disco > 1 else 0
        
        for disco in discos:
            disco_div = document.createElement("div")
            disco_div.className = "disco"
            disco_width = min_width + (disco - 1) * step
            disco_div.style.width = f"{disco_width}px"
            disco_div.textContent = str(disco)
            discos_container.appendChild(disco_div)

def atualizar_interface_movimentos():
    """Atualiza a lista de movimentos na interface"""
    container = document.getElementById("movimentos-container")
    container.innerHTML = ""
    
    if not movimentos_globais:
        empty_state = document.createElement("div")
        empty_state.className = "empty-state"
        empty_state.innerHTML = """
            <p>✨ Clique em "Mostrar Solução" para ver os movimentos</p>
            <p class="small">A função recursiva em Python resolve automaticamente!</p>
        """
        container.appendChild(empty_state)
        return
    
    for i, mov in enumerate(movimentos_globais, 1):
        div = document.createElement("div")
        div.className = "movimento-item"
        div.innerHTML = f"<strong>{i:3d}.</strong> {mov}"
        container.appendChild(div)
    
    # Rolar para o final
    container.scrollTop = container.scrollHeight
    
    # Atualizar contador
    count_element = document.getElementById("movimentos-lista-count")
    if count_element:
        count_element.textContent = f"{len(movimentos_globais)} movimentos"

def mostrar_mensagem(mensagem, tipo="info"):
    """Exibe mensagem temporária na interface"""
    msg_div = document.getElementById("status-message")
    msg_div.textContent = mensagem
    msg_div.className = f"status-message {tipo}"
    
    # Esconder após 3 segundos
    window.setTimeout(lambda: esconder_mensagem(), 3000)

def esconder_mensagem():
    msg_div = document.getElementById("status-message")
    msg_div.textContent = ""
    msg_div.className = "status-message"

def resolver_hanoi(event=None):
    """Função principal chamada pelo botão"""
    global movimentos_globais, hastes_atuais, num_discos_atual
    
    try:
        # Pegar número de discos do input
        input_discos = document.getElementById("num-discos")
        n = int(input_discos.value)
        num_discos_atual = n
        
        if n < 1 or n > 8:
            mostrar_mensagem("Por favor, use um número entre 1 e 8", "error")
            return
        
        # Limpar movimentos anteriores
        movimentos_globais = []
        
        # Inicializar hastes
        hastes_atuais = {
            'A': list(range(n, 0, -1)),
            'B': [],
            'C': []
        }
        
        # Desenhar estado inicial
        desenhar_hastes()
        
        # Atualizar informações
        document.getElementById("move-count").innerHTML = "0"
        minimo_teorico = 2**n - 1
        document.getElementById("min-moves").innerHTML = str(minimo_teorico)
        document.getElementById("disk-count").innerHTML = str(n)
        
        mostrar_mensagem(f"🔄 Resolvendo Torre de Hanói com {n} discos...", "info")
        
        # Executar função recursiva
        total_movimentos = torre_hanoi_recursivo(n, 'A', 'C', 'B')
        
        # Atualizar contadores
        document.getElementById("move-count").innerHTML = str(total_movimentos)
        
        # Mostrar resultados
        atualizar_interface_movimentos()
        
        if total_movimentos == minimo_teorico:
            mostrar_mensagem(f"✅ Solução ótima encontrada! {total_movimentos} movimentos.", "success")
        else:
            mostrar_mensagem(f"✅ Solução encontrada com {total_movimentos} movimentos (mínimo: {minimo_teorico})", "success")
        
        console.log(f"Resolvido! {total_movimentos} movimentos")
        
    except Exception as e:
        console.log(f"Erro: {str(e)}")
        mostrar_mensagem(f"Erro ao resolver: {str(e)}", "error")

def limpar_movimentos(event=None):
    """Limpa todos os movimentos e reinicia a visualização"""
    global movimentos_globais, hastes_atuais, num_discos_atual
    
    movimentos_globais = []
    
    # Reiniciar hastes com o estado inicial
    if hastes_atuais:
        n = num_discos_atual
        hastes_atuais = {
            'A': list(range(n, 0, -1)),
            'B': [],
            'C': []
        }
        desenhar_hastes()
    
    document.getElementById("move-count").innerHTML = "0"
    atualizar_interface_movimentos()
    mostrar_mensagem("🧹 Movimentos limpos! Clique em 'Mostrar Solução' para resolver novamente.", "info")

# Registrar funções no escopo global
from pyscript import window
window.resolver_hanoi = resolver_hanoi
window.limpar_movimentos = limpar_movimentos

# Inicializar ao carregar
def init():
    """Inicializa o jogo"""
    global hastes_atuais, num_discos_atual
    n = 3  # valor padrão
    num_discos_atual = n
    hastes_atuais = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    desenhar_hastes()
    document.getElementById("min-moves").innerHTML = str(2**n - 1)
    document.getElementById("disk-count").innerHTML = str(n)

# Executar inicialização
init()
