def menu():
    print("\n=== Cadastro de Alunos ===")
    print("1 - Cadastrar aluno")
    print("2 - Ver todos os cadastros")
    print("3 - Buscar cadastro")
    print("4 - Remover cadastro")
    print("5 - Sair")
    return input("Escolha uma opção: ")


def adicionar_cadastro(cadastro):
    print("\n--- Novo Contato ---")
    nome = input("Nome: ").strip().lower()
    nota = input("Nota: ")
    email = input("Email: ")

    cadastro[nome] = {"nota": nota, "email": email}
    print(f"\nCadastro do aluno '{nome}' realizado com sucesso!")


def ver_cadastros(cadastro):
    if not cadastro:
        print("\nNenhum aluno cadastrado.")
        return

    print("\n--- Lista de Alunos ---")
    for nome, info in cadastro.items():
        print(f"Nome: {nome.capitalize()}")
        print(f"  Nota: {info['nota']}")
        print(f"  Email: {info['email']}")
        print("-" * 20)


def buscar_cadastro(cadastro):
    if not cadastro:
        print("\nNenhum aluno cadastrado.")
        return

    nome = input("\nInsira o nome do aluno: ").strip().lower()

    if nome in cadastro:
        info = cadastro[nome]
        print(f"\n--- Contato Encontrado ---")
        print(f"Nome: {nome.capitalize()}")
        print(f"Nita: {info['nota']}")
        print(f"Email: {info['email']}")
    else:
        print(f"\nCadastro do aluno '{nome}' não encontrado.")


def remover_cadastro(cadastro):
    if not cadastro:
        print("\nNenhum aluno cadastrado.")
        return

    nome = input("\nInsira o nome do cadastro do aluno a remover: ").strip().lower()

    if nome in cadastro:
        del cadastro[nome]
        print(f"\nCadastro do aluno '{nome}' removido com sucesso!")
    else:
        print(f"\nCadastro do aluno '{nome}' não encontrado.")


cadastro = {}

while True:
    opcao = menu()

    if opcao == "1":
        adicionar_cadastro(cadastro)
    elif opcao == "2":
        ver_cadastros(cadastro)
    elif opcao == "3":
        buscar_cadastro(cadastro)
    elif opcao == "4":
        remover_cadastro(cadastro)
    elif opcao == "5":
        print("\nSaindo da Lista.")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
