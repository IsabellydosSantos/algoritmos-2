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

// Array para armazenar a sequência ótima de movimentos
let sequenciaOtima = [];

// ========== VARIÁVEIS DO CRONÔMETRO ==========
let cronometroAtivo = false;
let tempoInicio = 0;
let tempoDecorrido = 0;
let intervaloId = null;

// ========== FUNÇÃO RECURSIVA PARA GERAR SOLUÇÃO ÓTIMA ==========
function gerarSolucaoOtima(n, origem, destino, auxiliar) {
    let movimentos = [];
    
    if (n === 1) {
        movimentos.push([origem, destino]);
        return movimentos;
    }
    
    movimentos = movimentos.concat(gerarSolucaoOtima(n - 1, origem, auxiliar, destino));
    movimentos.push([origem, destino]);
    movimentos = movimentos.concat(gerarSolucaoOtima(n - 1, auxiliar, destino, origem));
    
    return movimentos;
}

function calcularSequenciaOtima() {
    sequenciaOtima = gerarSolucaoOtima(numDiscos, 'A', 'C', 'B');
}

// ========== FUNÇÕES DO CRONÔMETRO ==========
function iniciarCronometro() {
    if (intervaloId !== null) return;
    
    cronometroAtivo = true;
    tempoInicio = Date.now() - tempoDecorrido;
    
    intervaloId = setInterval(() => {
        if (cronometroAtivo && !gameWon) {
            tempoDecorrido = Date.now() - tempoInicio;
            atualizarDisplayCronometro();
        }
    }, 100);
}

function pararCronometro() {
    cronometroAtivo = false;
    if (intervaloId !== null) {
        clearInterval(intervaloId);
        intervaloId = null;
    }
}

function resetarCronometro() {
    pararCronometro();
    tempoDecorrido = 0;
    atualizarDisplayCronometro();
}

function atualizarDisplayCronometro() {
    const totalSegundos = Math.floor(tempoDecorrido / 1000);
    const minutos = Math.floor(totalSegundos / 60);
    const segundos = totalSegundos % 60;
    const milesimos = Math.floor((tempoDecorrido % 1000) / 10);
    
    const tempoFormatado = `${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}:${milesimos.toString().padStart(2, '0')}`;
    
    const cronometroDisplay = document.getElementById('cronometro');
    if (cronometroDisplay) {
        cronometroDisplay.innerHTML = `⏱️ ${tempoFormatado}`;
    }
}

function getTempoFormatado() {
    const totalSegundos = Math.floor(tempoDecorrido / 1000);
    const minutos = Math.floor(totalSegundos / 60);
    const segundos = totalSegundos % 60;
    const milesimos = Math.floor((tempoDecorrido % 1000) / 10);
    return `${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}:${milesimos.toString().padStart(2, '0')}`;
}

// ========== FUNÇÃO PARA ARRASTAR O CRONÔMETRO ==========
function tornarMovel(elemento) {
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    let movendo = false;
    
    elemento.onmousedown = function(e) {
        e.preventDefault();
        
        pos3 = e.clientX;
        pos4 = e.clientY;
        
        movendo = true;
        
        document.onmouseup = function() {
            movendo = false;
            document.onmouseup = null;
            document.onmousemove = null;
            elemento.style.cursor = 'move';
        };
        
        document.onmousemove = function(e) {
            if (!movendo) return;
            
            e.preventDefault();
            
            pos1 = pos3 - e.clientX;
            pos2 = pos4 - e.clientY;
            pos3 = e.clientX;
            pos4 = e.clientY;
            
            let topAtual = elemento.offsetTop - pos2;
            let leftAtual = elemento.offsetLeft - pos1;
            
            const maxX = window.innerWidth - elemento.offsetWidth;
            const maxY = window.innerHeight - elemento.offsetHeight;
            
            leftAtual = Math.max(0, Math.min(leftAtual, maxX));
            topAtual = Math.max(0, Math.min(topAtual, maxY));
            
            elemento.style.top = topAtual + 'px';
            elemento.style.left = leftAtual + 'px';
            elemento.style.right = 'auto';
        };
        
        elemento.style.cursor = 'grabbing';
    };
    
    elemento.ondragstart = function() {
        return false;
    };
}

// ========== FIM DAS FUNÇÕES DO CRONÔMETRO ==========

function inicializarJogo(discoCount = null) {
    if (discoCount === null) {
        const input = document.getElementById('diskSelector');
        if (input) {
            numDiscos = parseInt(input.value);
        }
    } else {
        numDiscos = discoCount;
    }
    
    if (isNaN(numDiscos) || numDiscos < 1 || numDiscos > 8) {
        numDiscos = 3;
        if (document.getElementById('diskSelector')) {
            document.getElementById('diskSelector').value = 3;
        }
        mostrarMensagem('Usando 3 discos (valor padrão: 1-8)', 'error');
    }
    
    if (document.getElementById('diskSelector')) {
        document.getElementById('diskSelector').value = numDiscos;
    }
    
    hastes = {
        A: [...Array(numDiscos).keys()].map(i => numDiscos - i),
        B: [],
        C: []
    };
    moveCount = 0;
    selectedPeg = null;
    gameWon = false;
    
    // Resetar e parar cronômetro
    resetarCronometro();
    pararCronometro();
    
    // Calcular a sequência ótima para a quantidade atual de discos
    calcularSequenciaOtima();
    
    document.getElementById('victoryArea').innerHTML = '';
    atualizarInterface();
}

function aplicarDiscos() {
    const input = document.getElementById('diskSelector');
    let novoNumero = parseInt(input.value);
    
    if (isNaN(novoNumero) || novoNumero < 1 || novoNumero > 8) {
        mostrarMensagem('Por favor, escolha um número entre 1 e 8!', 'error');
        input.value = numDiscos;
        return;
    }
    
    if (novoNumero !== numDiscos) {
        numDiscos = novoNumero;
        inicializarJogo(numDiscos);
        mostrarMensagem(`Jogo reiniciado com ${numDiscos} discos!`, 'success');
    } else {
        mostrarMensagem(`Já está com ${numDiscos} discos!`, 'success');
    }
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
    
    // Resetar e parar cronômetro
    resetarCronometro();
    pararCronometro();
    
    // Recalcular a sequência ótima
    calcularSequenciaOtima();
    
    document.getElementById('victoryArea').innerHTML = '';
    atualizarInterface();
    mostrarMensagem('Jogo reiniciado!', 'success');
}

function novoJogo() {
    const input = document.getElementById('diskSelector');
    const novoNumero = parseInt(input.value);
    
    if (!isNaN(novoNumero) && novoNumero >= 1 && novoNumero <= 8) {
        numDiscos = novoNumero;
    }
    
    inicializarJogo(numDiscos);
    mostrarMensagem('Novo jogo iniciado!', 'success');
}

function movimentoValido(origem, destino) {
    if (hastes[origem].length === 0) {
        return false;
    }
    
    const discoOrigem = hastes[origem][hastes[origem].length - 1];
    
    if (hastes[destino].length > 0) {
        const discoDestino = hastes[destino][hastes[destino].length - 1];
        if (discoOrigem > discoDestino) {
            return false;
        }
    }
    
    return true;
}

function realizarMovimento(origem, destino) {
    // Iniciar cronômetro no primeiro movimento
    if (moveCount === 0 && !gameWon) {
        iniciarCronometro();
    }
    
    if (!movimentoValido(origem, destino)) {
        mostrarMensagem(`❌ Movimento inválido!`, 'error');
        return false;
    }
    
    const disco = hastes[origem].pop();
    hastes[destino].push(disco);
    moveCount++;
    
    mostrarMensagem(`✅ Moveu disco ${disco} da haste ${origem} para haste ${destino}`, 'success');
    atualizarInterface();
    
    if (hastes.C.length === numDiscos) {
        const minimoTeorico = Math.pow(2, numDiscos) - 1;
        gameWon = true;
        
        // Parar cronômetro quando vencer
        pararCronometro();
        
        const tempoFinal = getTempoFormatado();
        
        const victoryHtml = `
            <div class="victory-message">
                🎉 PARABÉNS! VOCÊ VENCEU! 🎉<br>
                Movimentos: ${moveCount} | Mínimo teórico: ${minimoTeorico}<br>
                Tempo: ${tempoFinal}<br>
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
        if (hastes[peg].length === 0) {
            mostrarMensagem(`❌ Haste ${peg} está vazia!`, 'error');
            return;
        }
        selectedPeg = peg;
        mostrarMensagem(`📍 Haste ${peg} selecionada. Clique no destino.`, 'success');
        atualizarInterface();
    } else {
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
    messageArea.innerHTML = msg;
    messageArea.className = `message-area ${tipo === 'error' ? 'error-message' : 'success-message'}`;
    
    setTimeout(() => {
        if (document.getElementById('messageArea').innerHTML === msg) {
            messageArea.innerHTML = '';
            messageArea.className = 'message-area';
        }
    }, 3000);
}

function mostrarDica() {
    if (gameWon) {
        mostrarMensagem("🎉 O jogo já foi concluído! Comece um novo jogo.", 'error');
        return;
    }
    
    if (sequenciaOtima.length === 0) {
        calcularSequenciaOtima();
    }
    
    if (moveCount >= sequenciaOtima.length) {
        mostrarMensagem("🤔 Você já deveria ter vencido! Algo deu errado.", 'error');
        return;
    }
    
    const proximoMovimento = sequenciaOtima[moveCount];
    const [origemCorreta, destinoCorreto] = proximoMovimento;
    
    if (hastes[origemCorreta].length === 0) {
        mostrarMensagem(`⚠️ A sequência ótima diz para mover da haste ${origemCorreta} para ${destinoCorreto}, mas a haste ${origemCorreta} está vazia. Você pode ter se desviado da solução ótima. Tente reiniciar se quiser seguir o caminho mínimo.`, 'success');
        return;
    }
    
    const disco = hastes[origemCorreta][hastes[origemCorreta].length - 1];
    const movimentosRestantes = sequenciaOtima.length - moveCount;
    
    let mensagem = `🎯 DICA: Mova o disco ${disco} da haste ${origemCorreta} para a haste ${destinoCorreto}. `;
    
    if (movimentosRestantes === 1) {
        mensagem += `🚀 Este é o ÚLTIMO movimento! Você vai vencer!`;
    } else if (moveCount === 0) {
        mensagem += `📚 Este é o primeiro movimento da solução mínima de ${sequenciaOtima.length} movimentos.`;
    } else {
        mensagem += `📊 Faltam ${movimentosRestantes} movimentos para vencer no mínimo.`;
    }
    
    mostrarMensagem(mensagem, 'success');
}

function atualizarInterface() {
    const container = document.getElementById('hanoiContainer');
    container.innerHTML = '';
    
    const hastesOrder = ['A', 'B', 'C'];
    
    const coresDiscos = [
        { gradiente: 'linear-gradient(135deg, #FF6B6B, #FF5252)', cor: '#FF5252' },
        { gradiente: 'linear-gradient(135deg, #FFB74D, #FF9800)', cor: '#FF9800' },
        { gradiente: 'linear-gradient(135deg, #FFD54F, #FFC107)', cor: '#FFC107' },
        { gradiente: 'linear-gradient(135deg, #81C784, #4CAF50)', cor: '#4CAF50' },
        { gradiente: 'linear-gradient(135deg, #64B5F6, #2196F3)', cor: '#2196F3' },
        { gradiente: 'linear-gradient(135deg, #9575CD, #673AB7)', cor: '#673AB7' },
        { gradiente: 'linear-gradient(135deg, #F06292, #E91E63)', cor: '#E91E63' },
        { gradiente: 'linear-gradient(135deg, #4DB6AC, #009688)', cor: '#009688' }
    ];
    
    hastesOrder.forEach(haste => {
        const pegDiv = document.createElement('div');
        pegDiv.className = `peg ${selectedPeg === haste ? 'selected' : ''}`;
        pegDiv.onclick = () => handlePegClick(haste);
        
        const disksContainer = document.createElement('div');
        disksContainer.className = 'disks-container';
        
        const discos = hastes[haste];
        const maxDiskSize = 180;
        const minDiskSize = 40;
        const step = (maxDiskSize - minDiskSize) / (numDiscos - 1);
        
        discos.forEach(disco => {
            const diskDiv = document.createElement('div');
            let diskWidth;
            if (numDiscos === 1) {
                diskWidth = (maxDiskSize + minDiskSize) / 2;
            } else {
                diskWidth = minDiskSize + (disco - 1) * step;
            }
            diskDiv.className = 'disk';
            diskDiv.style.width = `${diskWidth}px`;
            
            const corIndex = (disco - 1) % coresDiscos.length;
            diskDiv.style.background = coresDiscos[corIndex].gradiente;
            diskDiv.style.border = `2px solid ${coresDiscos[corIndex].cor}`;
            diskDiv.style.borderBottom = `4px solid ${coresDiscos[corIndex].cor}`;
            
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
        
        pegDiv.appendChild(stickDiv);
        pegDiv.appendChild(baseDiv);
        pegDiv.appendChild(disksContainer);
        pegDiv.appendChild(labelDiv);
        
        container.appendChild(pegDiv);
    });
    
    document.getElementById('moveCount').textContent = moveCount;
    document.getElementById('minMoves').textContent = Math.pow(2, numDiscos) - 1;
    document.getElementById('diskCount').textContent = numDiscos;
}

document.addEventListener('DOMContentLoaded', () => {
    inicializarJogo();
    
    document.getElementById('newGameBtn').addEventListener('click', novoJogo);
    document.getElementById('resetGameBtn').addEventListener('click', resetarJogo);
    document.getElementById('applyDiscsBtn').addEventListener('click', aplicarDiscos);
    document.getElementById('hintBtn').addEventListener('click', mostrarDica);
    
    const diskInput = document.getElementById('diskSelector');
    if (diskInput) {
        diskInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                aplicarDiscos();
            }
        });
    }
    
    // Tornar o cronômetro móvel
    const cronometroElemento = document.getElementById('cronometro');
    if (cronometroElemento) {
        cronometroElemento.style.position = 'fixed';
        cronometroElemento.style.top = '20px';
        cronometroElemento.style.right = '20px';
        cronometroElemento.style.cursor = 'move';
        
        tornarMovel(cronometroElemento);
    }
});
