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

// Variáveis para dica automática
let ultimoMovimento = Date.now();
let tempoSemMovimento = null;

function inicializarJogo(discoCount = null) {
    // Se um número foi passado, usa ele; senão, pega do input
    if (discoCount === null) {
        const input = document.getElementById('diskSelector');
        if (input) {
            numDiscos = parseInt(input.value);
        }
    } else {
        numDiscos = discoCount;
    }
    
    // Validação para 1-8 discos
    if (isNaN(numDiscos) || numDiscos < 1 || numDiscos > 8) {
        numDiscos = 3;
        if (document.getElementById('diskSelector')) {
            document.getElementById('diskSelector').value = 3;
        }
        mostrarMensagem('Usando 3 discos (valor padrão: 1-8)', 'error');
    }
    
    // Atualiza o input com o valor válido
    if (document.getElementById('diskSelector')) {
        document.getElementById('diskSelector').value = numDiscos;
    }
    
    // Inicializa as hastes
    hastes = {
        A: [...Array(numDiscos).keys()].map(i => numDiscos - i),
        B: [],
        C: []
    };
    moveCount = 0;
    selectedPeg = null;
    gameWon = false;
    ultimoMovimento = Date.now();
    document.getElementById('victoryArea').innerHTML = '';
    atualizarInterface();
}

function aplicarDiscos() {
    const input = document.getElementById('diskSelector');
    let novoNumero = parseInt(input.value);
    
    // Validação para 1-8 discos
    if (isNaN(novoNumero) || novoNumero < 1 || novoNumero > 8) {
        mostrarMensagem('Por favor, escolha um número entre 1 e 8!', 'error');
        input.value = numDiscos; // Restaura o valor anterior
        return;
    }
    
    // Se o número mudou, reinicia o jogo
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
    ultimoMovimento = Date.now();
    document.getElementById('victoryArea').innerHTML = '';
    atualizarInterface();
    mostrarMensagem('Jogo reiniciado!', 'success');
}

function novoJogo() {
    // Pega o valor atual do input
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
    // Atualizar timer para dica automática
    ultimoMovimento = Date.now();
    if (tempoSemMovimento !== null) {
        clearTimeout(tempoSemMovimento);
        tempoSemMovimento = null;
    }
    
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
    messageArea.innerHTML = msg;
    messageArea.className = `message-area ${tipo === 'error' ? 'error-message' : 'success-message'}`;
    
    setTimeout(() => {
        if (document.getElementById('messageArea').innerHTML === msg) {
            messageArea.innerHTML = '';
            messageArea.className = 'message-area';
        }
    }, 3000);
}

// Função para encontrar o melhor movimento (dica inteligente)
function encontrarDica() {
    if (gameWon) {
        return { 
            valido: false, 
            mensagem: "🎉 O jogo já foi concluído! Comece um novo jogo para praticar." 
        };
    }
    
    const hastesLista = ['A', 'B', 'C'];
    
    // 1. Verificar se há algum movimento que leve à vitória
    for (let origem of hastesLista) {
        if (hastes[origem].length === 0) continue;
        
        const discoOrigem = hastes[origem][hastes[origem].length - 1];
        
        for (let destino of hastesLista) {
            if (origem === destino) continue;
            
            if (destino === 'C' && hastes[destino].length === numDiscos - 1 && 
                (hastes[destino].length === 0 || discoOrigem < hastes[destino][hastes[destino].length - 1])) {
                return {
                    valido: true,
                    origem: origem,
                    destino: destino,
                    disco: discoOrigem,
                    mensagem: `🎯 DICA ESPECIAL: Mova o disco ${discoOrigem} da haste ${origem} para a haste ${destino}! Isso vai te deixar a apenas 1 movimento da vitória!`
                };
            }
        }
    }
    
    // 2. Buscar o menor disco que pode ser movido
    let melhorMovimento = null;
    let menorDisco = Infinity;
    
    for (let origem of hastesLista) {
        if (hastes[origem].length === 0) continue;
        
        const discoOrigem = hastes[origem][hastes[origem].length - 1];
        
        for (let destino of hastesLista) {
            if (origem === destino) continue;
            
            if (hastes[destino].length === 0 || discoOrigem < hastes[destino][hastes[destino].length - 1]) {
                if (discoOrigem < menorDisco) {
                    menorDisco = discoOrigem;
                    melhorMovimento = {
                        origem: origem,
                        destino: destino,
                        disco: discoOrigem
                    };
                }
            }
        }
    }
    
    // 3. Se encontrou um movimento válido
    if (melhorMovimento) {
        const { origem, destino, disco } = melhorMovimento;
        
        if (disco === 1) {
            return {
                valido: true,
                origem: origem,
                destino: destino,
                disco: disco,
                mensagem: `💡 DICA: O disco 1 (menor) pode ser movido da haste ${origem} para a haste ${destino}! Aproveite que ele é o mais versátil.`
            };
        } else if (hastes[destino].length === 0) {
            return {
                valido: true,
                origem: origem,
                destino: destino,
                disco: disco,
                mensagem: `💡 DICA: Mova o disco ${disco} da haste ${origem} para a haste ${destino} (está vazia)! É um movimento válido.`
            };
        } else {
            return {
                valido: true,
                origem: origem,
                destino: destino,
                disco: disco,
                mensagem: `💡 DICA: Mova o disco ${disco} da haste ${origem} para a haste ${destino}! Ele é menor que o disco ${hastes[destino][hastes[destino].length - 1]} no topo da haste ${destino}.`
            };
        }
    }
    
    return {
        valido: false,
        mensagem: "🤔 Não encontrei nenhum movimento válido no momento. Tente reiniciar o jogo!"
    };
}

// Função para mostrar a dica na interface
function mostrarDica() {
    const dica = encontrarDica();
    const messageArea = document.getElementById('messageArea');
    
    if (dica.valido) {
        messageArea.innerHTML = dica.mensagem;
        messageArea.className = 'message-area hint-message';
        
        setTimeout(() => {
            if (document.getElementById('messageArea').innerHTML === dica.mensagem) {
                messageArea.innerHTML = '';
                messageArea.className = 'message-area';
            }
        }, 5000);
    } else {
        mostrarMensagem(dica.mensagem, 'error');
    }
}

// Função para dar dica automática
function verificarDicaAutomatica() {
    if (gameWon) return;
    
    const tempoAtual = Date.now();
    const tempoParado = (tempoAtual - ultimoMovimento) / 1000;
    
    if (tempoParado > 30 && tempoSemMovimento === null) {
        tempoSemMovimento = setTimeout(() => {
            if (!gameWon && (Date.now() - ultimoMovimento) > 30000) {
                mostrarDica();
                mostrarMensagem("⏰ Você está há algum tempo sem mover! Aqui vai uma dica:", 'success');
            }
            tempoSemMovimento = null;
        }, 30000);
    } else if (tempoParado < 30 && tempoSemMovimento !== null) {
        clearTimeout(tempoSemMovimento);
        tempoSemMovimento = null;
    }
}

function atualizarInterface() {
    const container = document.getElementById('hanoiContainer');
    container.innerHTML = '';
    
    const hastesOrder = ['A', 'B', 'C'];
    
    // Paleta de cores em gradiente arco-íris suaves
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

// Configurar event listeners quando a página carregar
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
    
    setInterval(() => {
        verificarDicaAutomatica();
    }, 5000);
});
