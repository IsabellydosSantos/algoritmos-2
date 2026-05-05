def ler_arquivo(nome, separador):
    lista = []

    try:
        with open(nome, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip('\n')
                if linha:
                    campos = linha.split(separador)
                    lista.append(campos)
        return lista

    except FileNotFoundError:
        print(f"Erro: Arquivo {nome} não encontrado")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
