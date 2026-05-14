def calcular_saldo(nome_arquivo):
    saldo = 0
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                if linha.strip():
                    partes = linha.split()
                    valor = int(partes[0])
                    saldo += valor
        
        print(f"Saldo financeiro final: R$ {saldo}")
        return saldo
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado")
        return None

calcular_saldo("financeiro.txt")
