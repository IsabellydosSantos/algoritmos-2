def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return 1
    
    movimentos = 0
    # Mover n-1 discos da origem para o auxiliar
    movimentos += torre_hanoi_recursivo(n-1, origem, auxiliar, destino)
    
    # Mover o disco maior da origem para o destino
    print(f"Mover disco {n} de {origem} para {destino}")
    movimentos += 1
    
    # Mover n-1 discos do auxiliar para o destino
    movimentos += torre_hanoi_recursivo(n-1, auxiliar, destino, origem)
    
    return movimentos

def jogar_hanoi():
    print("=== Torre de Hanói - Versão Recursiva ===")
    try:
        n = int(input("Digite o número de discos (1-8): "))
        if n < 1 or n > 8:
            print("Por favor, digite um número entre 1 e 8")
            return
        
        print(f"\nResolvendo Torre de Hanói com {n} discos:")
        print("-" * 40)
        
        movimentos = torre_hanoi_recursivo(n, 'A', 'C', 'B')
        
        print("-" * 40)
        print(f"Total de movimentos necessários: {movimentos}")
        print(f"Mínimo teórico: {2**n - 1} movimentos")
        
    except ValueError:
        print("Por favor, digite um número válido!")


jogar_hanoi_recursivo()
