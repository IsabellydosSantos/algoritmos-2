def inverter_arquivo():
    try:
        with open("pares.txt", "r", encoding='utf-8') as original:
            linhas = [linha.strip() for linha in original if linha.strip()]
        
        linhas_invertidas = linhas[::-1]
        
        with open("pares_invertido.txt", "w", encoding='utf-8') as invertido:
            for linha in linhas_invertidas:
                invertido.write(f"{linha}\n")
        
        print("Arquivo 'pares_invertido.txt' criado")
        #print(f"Ordem original: {linhas}")
        #print(f"Ordem invertida: {linhas_invertidas}")
        
    except FileNotFoundError:
        print("Arquivo 'pares.txt' não encontrado")

inverter_arquivo()
