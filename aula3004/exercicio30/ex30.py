def adicionar_registro():
    valor = int(input("Digite o valor (ex: 500 ou -200): "))
    descricao = input("Digite a descrição: ")
    
    with open("financeiro.txt", "a", encoding='utf-8') as arquivo:
        arquivo.write(f"{valor} {descricao}\n")
    
    print(f"Registro adicionado: {valor} {descricao}")

adicionar_registro()
