def mostrar_menu():
    print("Agenda de Contatos")
    print("1 - Adicionar contato")
    print("2 - Ver todos os contatos")
    print("3 - Buscar contato")
    print("4 - Excluir contato")
    print("5 - Sair")
    return input("Escolha uma opção: ")


def adicionar_contato(agenda):
    print("Novo contato")
    nome = input("Nome: ").strip().lower()
    telefone = input("Telefone: ")
    email = input("Email: ")

    agenda[nome] = {"nome": nome, "telefone": telefone, "email": email}
    print(f"Contato {nome} adicionado")


def ver_contato(agenda):
    if not agenda:
        print("Nenhum contato cadastrado")
        return

    print("Lista de Contatos")
    for nome, info in agenda.items():
        print(f"Nome: {nome.capitalize()}")
        print(f"Telefone: {info['telefone']}")
        print(f"Email: {info['email']}")


def buscar_contato(agenda):
    if not agenda:
        print("Nenhum contato cadastrado")
        return

    nome = input("Insira o nome do contato: ").strip().lower()

    if nome in agenda:
        info = agenda[nome]
        print("Contato encontrado")
        print(f"Nome:")
