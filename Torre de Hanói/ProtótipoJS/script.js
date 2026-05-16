// Estado do jogo
let hastes = {
    A: [],
    B: [],
    C: []
};
let selectedPeg = null;
let moveCount = 0;
let numDiscos = 3;
let gameWon = false;

function inicializarJogo() {
    numDiscos = parseInt(prompt("Digite o número de discos (1-6):", "3"));
    if (isNaN(numDiscos) || numDiscos < 1 || numDiscos > 6) {
        numDiscos = 3;
        alert("Usando 3 discos (valor padrão)");
    }
    
    hastes = {
        A: [...Array(numDiscos).keys()].map(i => numDiscos - i),
        B: [],
        C: []
    };
    moveCount = 0;
    selectedPeg = null;
    gameWon = false;
    atualizarInterface();
}

function resetarJogo() {
    hastes = {
        A: [...Array(numDiscos).keys()].map(i => numDiscos - i),
        B: [],
        C: []
    };
    moveCount = 0;
    selectedPeg = null;
    gameWon = false;
    document.getElementById('victoryArea').innerHTML = '';
    atualizarInterface();
    mostrarMensagem('Jogo reiniciado!', 'success');
}

function novoJogo() {
    inicializarJogo();
    mostrarMensagem('Novo jogo iniciado!', 'success');
}

function movimentoValido(origem, destino) {
    if (hastes[origem].length === 0) {
        mostrarMensagem('❌ Esta haste está vazia!', 'error');
        return false;
    }
    
    const discoOrigem = hastes[origem][hastes[origem].length - 1];
    
    if (hastes[destino].length > 0) {
        const discoDestino = hastes[destino][hastes[destino].length - 1];
        if (discoOrigem > discoDestino) {
            mostrarMensagem(`❌ Não pode colocar disco ${discoOrigem} sobre o disco ${discoDestino}!`, 'error');
            return false;
        }
    }
    
    return true;
}

function realizarMovimento(origem, destino) {
    if (!movimentoValido(origem, destino)) {
        return false;
    }
    
    const disco = hastes[origem].pop();
    hastes[destino].push(disco);
    moveCount++;
    
    mostrarMensagem(`✅ Moveu disco ${disco} da haste ${origem} para haste ${destino}`, 'success');
    atualizarInterface();
    
    // Verificar vitória
    if (hastes.C.length === numDiscos) {
        const minimoTeorico = Math.pow(2, numDiscos) - 1;
        gameWon = true;
        const victoryHtml = `
            <div class="victory-message">
                🎉 PARABÉNS! VOCÊ VENCEU! 🎉<br>
                Movimentos: ${moveCount} | Mínimo teórico: ${minimoTeorico}<br>
                ${moveCount === minimoTeorico ? '⭐ PERFEITO! Você fez o mínimo de movimentos! ⭐' : 
                  `💪 Você fez ${moveCount - minimoTeorico} movimentos extras. Tente melhorar!`}
            </div>
        `;
        document.getElementById('victoryArea').innerHTML = victoryHtml;
        mostrarMensagem('🎉 VITÓRIA! Parabéns! 🎉', 'success');
    }
    
    return true;
}

function handlePegClick(peg) {
    if (gameWon) {
        mostrarMensagem('Jogo já terminado! Clique em "Novo Jogo" para continuar', 'error');
        return;
    }
    
    if (selectedPeg === null) {
        // Selecionar haste de origem
        if (hastes[peg].length === 0) {
            mostrarMensagem(`❌ Haste ${peg} está vazia! Escolha outra haste.`, 'error');
            return;
        }
        selectedPeg = peg;
        mostrarMensagem(`📍 Haste ${peg} selecionada. Agora clique na haste de destino.`, 'success');
        atualizarInterface();
    } else {
        // Mover da haste selecionada para a haste clicada
        if (selectedPeg === peg) {
            mostrarMensagem('⚠️ Origem e destino não podem ser iguais!', 'error');
            selectedPeg = null;
            atualizarInterface();
            return;
        }
        
        realizarMovimento(selectedPeg, peg);
        selectedPeg = null;
        atualizarInterface();
    }
}

function mostrarMensagem(msg, tipo) {
    const messageArea = document.getElementById('messageArea');
    messageArea.textContent = msg;
    messageArea.className = `message-area ${tipo === 'error' ? 'error-message' : 'success-message'}`;
    
    setTimeout(() => {
        if (document.getElementById('messageArea').textContent === msg) {
            messageArea.textContent = '';
            messageArea.className = 'message-area';
        }
    }, 2000);
}

function atualizarInterface() {
    const container = document.getElementById('hanoiContainer');
    container.innerHTML = '';
    
    const hastesOrder = ['A', 'B', 'C'];
    
    hastesOrder.forEach(haste => {
        const pegDiv = document.createElement('div');
        pegDiv.className = `peg ${selectedPeg === haste ? 'selected' : ''}`;
        pegDiv.onclick = () => handlePegClick(haste);
        
        const disksContainer = document.createElement('div');
        disksContainer.className = 'disks-container';
        
        const discos = hastes[haste];
        const maxDiskSize = 120; // pixels
        const minDiskSize = 40;
        const step = (maxDiskSize - minDiskSize) / numDiscos;
        
        discos.forEach(disco => {
            const diskDiv = document.createElement('div');
            const diskWidth = minDiskSize + (disco - 1) * step;
            diskDiv.className = 'disk';
            diskDiv.style.width = `${diskWidth}px`;
            diskDiv.textContent = disco;
            disksContainer.appendChild(diskDiv);
        });
        
        const stickDiv = document.createElement('div');
        stickDiv.className = 'peg-stick';
        
        const baseDiv = document.createElement('div');
        baseDiv.className = 'peg-base';
        
        const labelDiv = document.createElement('div');
        labelDiv.className = 'peg-label';
        labelDiv.textContent = `Haste ${haste}`;
        
        pegDiv.appendChild(disksContainer);
        pegDiv.appendChild(stickDiv);
        pegDiv.appendChild(baseDiv);
        pegDiv.appendChild(labelDiv);
        
        container.appendChild(pegDiv);
    });
    
    // Atualizar informações
    document.getElementById('moveCount').textContent = moveCount;
    document.getElementById('minMoves').textContent = Math.pow(2, numDiscos) - 1;
    document.getElementById('diskCount').textContent = numDiscos;
}

// Configurar event listeners quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    inicializarJogo();
    
    document.getElementById('newGameBtn').addEventListener('click', novoJogo);
    document.getElementById('resetGameBtn').addEventListener('click', resetarJogo);
});
