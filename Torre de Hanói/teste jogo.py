def exibir_hastes(hastes):
    print("\nEstado atual:")
    for haste in ['A', 'B', 'C']:
        print(f"Haste {haste}: {hastes[haste]}")
    print("-" * 30)

def movimento_valido(hastes, origem, destino):
    """Verifica se o movimento é permitido"""
    if not hastes[origem]:  # Haste de origem vazia
        print("Erro: Haste de origem está vazia!")
        return False
    
    disco_origem = hastes[origem][-1]
    
    if hastes[destino]:  # Se destino não está vazio
        disco_destino = hastes[destino][-1]
        if disco_origem > disco_destino:
            print("Erro: Não pode colocar um disco maior sobre um menor!")
            return False
    
    return True

def jogar():
    print("===== Torre de Hanói =====")
    
    try:
        n = int(input("Digite o número de discos (1-5): "))
        if n < 1 or n > 5:
            print("Por favor, digite um número entre 1 e 5")
            return
        
        # Inicializar hastes: A com discos (maior na base), B e C vazias
        hastes = {
            'A': list(range(n, 0, -1)),  # [n, n-1, ..., 1]
            'B': [],
            'C': []
        }
        
        movimentos = 0
        minimo_teorico = 2**n - 1
        
        print(f"\nObjetivo: Mover todos os discos da haste A para a haste C")
        print(f"Movimentos mínimos teóricos: {minimo_teorico}")
        
        while hastes['C'] != list(range(n, 0, -1)):
            exibir_hastes(hastes)
            print(f"Movimentos realizados: {movimentos}")
            
            try:
                origem = input("Digite a haste de origem (A/B/C): ").upper().strip()
                destino = input("Digite a haste de destino (A/B/C): ").upper().strip()
                
                if origem not in ['A', 'B', 'C'] or destino not in ['A', 'B', 'C']:
                    print("Erro: Hastes devem ser A, B ou C!")
                    continue
                
                if origem == destino:
                    print("Erro: Origem e destino não podem ser iguais!")
                    continue
                
                if movimento_valido(hastes, origem, destino):
                    # Realizar movimento
                    disco = hastes[origem].pop()
                    hastes[destino].append(disco)
                    movimentos += 1
                    print(f"\n✅ Moveu disco {disco} de {origem} para {destino}")
                else:
                    continue
                    
            except KeyboardInterrupt:
                print("\n\nJogo interrompido!")
                return
        
        print("\n" + "=" * 40)
        print("🎉 Parabéns! Você venceu! 🎉")
        print(f"Total de movimentos: {movimentos}")
        
        if movimentos == minimo_teorico:
            print("⭐ Você fez o número mínimo de movimentos!")
        else:
            print(f"Movimentos mínimos possíveis: {minimo_teorico}")
            print(f"Você fez {movimentos - minimo_teorico} movimentos extras")
        print("=" * 40)
        
    except ValueError:
        print("Insira apenas números válidos.")

jogar()
