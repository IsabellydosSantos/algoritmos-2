def arquivos(arq_par, arq_imp, arq_saida):
    try:
        numeros = []

        with open(arq_par, "r") as pares:
            for linha in pares:
                if linha.strip():
                    numeros.append(int(linha.strip()))

        with open(arq_imp, "r") as impares:
            for linha in impares:
                if linha.strip():
                    numeros.append(int(linha.strip()))

        numeros.sort()
        
        with open(arq_saida, "w") as ambos:
            for num in numeros:
                ambos.write(f"{num}\n")
        
        print(f"{len(numeros)} números salvos")
        return True
        
    except FileNotFoundError:
        print("Erro: Algum dos arquivos não foi encontrado")
        return False
    except ValueError:
        print("Erro: O arquivo contém algo que não é número")
        return False


resultado = arquivos("pares.txt", "impares.txt", "paresimpares.txt")

if resultado:
    print("Operação concluída")
else:
    print("Falha na operação")
    
