def arquivos(arq_par, arq_imp, arq_saida):
    try:
        numeros = []

        with open("pares.txt", "r") as pares:
            for linha in pares:
                if linha.strip():
                    numeros.append(int(linha.strip()))

        with open("impares.txt", "r") as impares:
            for linha in impares:
                if linha.strip():
                    numeros.append(int(linha.strip()))

        numeros.sort()
        with open("paresimpares.txt", "w") as ambos:
            for num in numeros:
                ambos.write(f"{num}\n")
                
    except FileNotFoundError:
        print(f"Erro: Algum dos arquivos não foi encontrado")
    except ValueError:
        print("Erro: O arquivo contém algo que não é um número")


arq_par = "pares.txt"
arq_impar = "impares.txt"
arq_saida = "paresimpares.txt"

resultado = arquivos(arq_par, arq_impar, arq_saida)

if not resultado:
    print("Erro. Verifique os arquivos e tente novamente")