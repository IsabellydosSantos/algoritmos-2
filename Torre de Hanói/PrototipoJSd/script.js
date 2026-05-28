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
let ultimoDiscoMovido = null;
let dicasDadas = [];

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
    ultimoMovimento = Date.now();
    ultimoDiscoMovido = null;
    dicasDadas = [];
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
    ultimoMovimento = Date.now();
    ultimoDiscoMovido = null;
    dicasDadas = [];
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
    ultimoMovimento = Date.now();
    if (tempoSemMovimento !== null) {
        clearTimeout(tempoSemMovimento);
        tempoSemMovimento = null;
    }
    
    if (!movimentoValido(origem, destino)) {
        mostrarMensagem(`❌ Movimento inválido!`, 'error');
        return false;
    }
    
    const disco = hastes[origem].pop();
    hastes[destino].push(disco);
    moveCount++;
    ultimoDiscoMovido = disco;
    
    mostrarMensagem(`✅ Moveu disco ${disco} da haste ${origem} para haste ${destino}`, 'success');
    atualizarInterface();
    
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

// FUNÇÃO DE DICA CORRETA - Baseada na lógica matemática da Torre de Hanói
function encontrarDica() {
    if (gameWon) {
        return { valido: false, mensagem: "🎉 O jogo já foi concluído!" };
    }
    
    // Mapeamento do sentido de rotação para cada disco
    // Disco 1 (menor) - sentido horário: A -> B -> C -> A
    // Disco 2 - sentido anti-horário: A -> C -> B -> A
    // Disco 3 - sentido horário (igual ao 1)
    // Disco 4 - sentido anti-horário (igual ao 2)
    // Padrão: discos ímpares (1,3,5,7) giram no sentido A->B->C->A
    //         discos pares (2,4,6,8) giram no sentido A->C->B->A
    
    function getProximaHaste(disco, hasteAtual) {
        const ordemImpar = ['A', 'B', 'C'];
        const ordemPar = ['A', 'C', 'B'];
        
        const ordem = (disco % 2 === 1) ? ordemImpar : ordemPar;
        const indexAtual = ordem.indexOf(hasteAtual);
        const proximoIndex = (indexAtual + 1) % 3;
        return ordem[proximoIndex];
    }
    
    // 1. Primeiro, encontrar o menor disco que pode ser movido (regra de ouro)
    let menorDiscoEncontrado = Infinity;
    let melhorOrigem = null;
    let melhorDestino = null;
    
    for (let haste of ['A', 'B', 'C']) {
        if (hastes[haste].length > 0) {
            const topo = hastes[haste][hastes[haste].length - 1];
            if (topo < menorDiscoEncontrado) {
                // Verificar se existe algum destino válido para este disco
                for (let destino of ['A', 'B', 'C']) {
                    if (haste !== destino && movimentoValido(haste, destino)) {
                        menorDiscoEncontrado = topo;
                        melhorOrigem = haste;
                        melhorDestino = destino;
                        break;
                    }
                }
            }
        }
    }
    
    // 2. Se encontrou o menor disco, verificar se ele está no caminho certo
    if (melhorOrigem && melhorDestino) {
        const disco = menorDiscoEncontrado;
        const destinoCorreto = getProximaHaste(disco, melhorOrigem);
        
        // Se o disco NÃO está indo para o lugar certo segundo o padrão
        if (melhorDestino !== destinoCorreto) {
            // Verificar se o destino correto é válido
            if (movimentoValido(melhorOrigem, destinoCorreto)) {
                return {
                    valido: true,
                    origem: melhorOrigem,
                    destino: destinoCorreto,
                    disco: disco,
                    mensagem: `🔮 DICA BASEADA NO PADRÃO: O disco ${disco} (${disco % 2 === 1 ? 'ímpar' : 'par'}) deve se mover da haste ${melhorOrigem} para a haste ${destinoCorreto}. Esta é a sequência ótima!`
                };
            }
        }
        
        // Se já está no caminho certo, sugerir o movimento
        return {
            valido: true,
            origem: melhorOrigem,
            destino: melhorDestino,
            disco: disco,
            mensagem: `✅ DICA: Mova o disco ${disco} (o menor que pode ser movido) da haste ${melhorOrigem} para a haste ${melhorDestino}.`
        };
    }
    
    // 3. Se não encontrou, buscar qualquer movimento válido que não repita o último disco
    for (let origem of ['A', 'B', 'C']) {
        if (hastes[origem].length === 0) continue;
        
        const disco = hastes[origem][hastes[origem].length - 1];
        
        // Regra: nunca mover o mesmo disco duas vezes seguidas
        if (disco === ultimoDiscoMovido) continue;
        
        for (let destino of ['A', 'B', 'C']) {
            if (origem !== destino && movimentoValido(origem, destino)) {
                return {
                    valido: true,
                    origem: origem,
                    destino: destino,
                    disco: disco,
                    mensagem: `💡 DICA: Mova o disco ${disco} da haste ${origem} para a haste ${destino}.`
                };
            }
        }
    }
    
    return {
        valido: false,
        mensagem: "🤔 Use a regra: nunca coloque um disco maior sobre um menor. Tente mover o menor disco possível!"
    };
}

function mostrarDica() {
    const dica = encontrarDica();
    const messageArea = document.getElementById('messageArea');
    
    if (dica.valido) {
        // Evitar dicas repetidas
        const chaveDica = `${dica.origem}${dica.destino}${dica.disco}`;
        if (dicasDadas.includes(chaveDica) && dicasDadas.length > 0) {
            // Dar uma dica alternativa
            for (let origem of ['A', 'B', 'C']) {
                if (hastes[origem].length > 0) {
                    const disco = hastes[origem][hastes[origem].length - 1];
                    for (let destino of ['A', 'B', 'C']) {
                        if (origem !== destino && movimentoValido(origem, destino) && 
                            `${origem}${destino}${disco}` !== chaveDica) {
                            messageArea.innerHTML = `🔄 Alternativa: Mova o disco ${disco} da haste ${origem} para a haste ${destino}. Tente seguir o padrão dos discos ${disco % 2 === 1 ? 'ímpares (A→B→C)' : 'pares (A→C→B)'}!`;
                            messageArea.className = 'message-area hint-message';
                            setTimeout(() => {
                                if (document.getElementById('messageArea').innerHTML === messageArea.innerHTML) {
                                    messageArea.innerHTML = '';
                                    messageArea.className = 'message-area';
                                }
                            }, 6000);
                            return;
                        }
                    }
                }
            }
        }
        
        dicasDadas.push(chaveDica);
        if (dicasDadas.length > 5) dicasDadas.shift();
        
        messageArea.innerHTML = dica.mensagem;
        messageArea.className = 'message-area hint-message';
        
        // Piscar as hastes sugeridas
        const hastesElements = document.querySelectorAll('.peg');
        const indices = { 'A': 0, 'B': 1, 'C': 2 };
        
        if (dica.origem && dica.destino) {
            hastesElements[indices[dica.origem]].style.transition = 'box-shadow 0.3s';
            hastesElements[indices[dica.origem]].style.boxShadow = '0 0 20px #f39c12';
            hastesElements[indices[dica.destino]].style.boxShadow = '0 0 20px #48bb78';
            
            setTimeout(() => {
                hastesElements.forEach(el => {
                    el.style.boxShadow = '';
                });
            }, 3000);
        }
        
        setTimeout(() => {
            if (document.getElementById('messageArea').innerHTML === dica.mensagem) {
                messageArea.innerHTML = '';
                messageArea.className = 'message-area';
            }
        }, 6000);
    } else {
        mostrarMensagem(dica.mensagem, 'error');
    }
}

function verificarDicaAutomatica() {
    if (gameWon) return;
    
    const tempoAtual = Date.now();
    const tempoParado = (tempoAtual - ultimoMovimento) / 1000;
    
    if (tempoParado > 30 && tempoSemMovimento === null) {
        tempoSemMovimento = setTimeout(() => {
            if (!gameWon && (Date.now() - ultimoMovimento) > 30000) {
                mostrarDica();
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
    
    setInterval(() => {
        verificarDicaAutomatica();
    }, 5000);
});
