def substituir(arquivo1, arquivo2, string1, string2):
    try:
        with open(arquivo1, "r") as original:
            conteudo = original.read()
        conteudo_mod = conteudo.replace(string1, string2)

        with open(arquivo2, 'w') as modif:
            modif.write(conteudo_mod)
        return True
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo1} não foi encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")
        return False


arquivo1 = input("Insira o nome do primeiro arquivo: ")
arquivo2 = input("Insira o nome do segundo arquivo: ")
string1 = input("Insira a primeira string: ")
string2 = input("Insira a segunda string: ")

resultado = substituir(arquivo1, arquivo2, string1, string2)

if resultado:
    print(f"Arquivo {arquivo2} criado com sucesso\nTodas as ocorrências de {string1} foram substituídas por {string2}")
else:
    print(f"Erro. Verifique os dados e tente novamente")
