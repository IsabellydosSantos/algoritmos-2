def calcular_medias_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print("Média dos estudantes")
            
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    campos = linha.split(',')
                    nome = campos[0]
                    notas = []
                    for nota in campos[1:]:
                        notas.append(float(nota))
                    
                    media = sum(notas) / len(notas)
                    
                    print(f"{nome:10} → média: {media:.2f}")
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado")
    except ValueError as e:
        print(f"Erro: O arquivo contém um valor inválido - {e}")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


print("Sistema de cálculo de médias \n")
calcular_medias_arquivo("notas.csv")
