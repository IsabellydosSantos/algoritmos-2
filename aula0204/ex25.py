def menu():
    print("\n=== Agenda de Contatos ===")
    print("1 - Adicionar contato")
    print("2 - Ver todos os contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair") 
    return input("Escolha uma opção: ")

def adicionar_contato(agenda):
    print("\n--- Novo Contato ---")
    nome = input("Nome: ").strip().lower()
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    agenda[nome] = {"telefone": telefone, "email": email}
    print(f"\nContato '{nome}' adicionado com sucesso!")

def ver_contatos(agenda):
    if not agenda:
        print("\nNenhum contato cadastrado.")
        return
    
    print("\n--- Lista de Contatos ---")
    for nome, info in agenda.items():
        print(f"Nome: {nome.capitalize()}")
        print(f"  Telefone: {info['telefone']}")
        print(f"  Email: {info['email']}")
        print("-" * 20)

def buscar_contato(agenda):
    if not agenda:
        print("\nNenhum contato cadastrado.")
        return
    
    nome = input("\nInsira o nome do contato: ").strip().lower()
    
    if nome in agenda:
        info = agenda[nome]
        print(f"\n--- Contato Encontrado ---")
        print(f"Nome: {nome.capitalize()}")
        print(f"Telefone: {info['telefone']}")
        print(f"Email: {info['email']}")
    else:
        print(f"\nContato '{nome}' não encontrado.")

def remover_contato(agenda):
    if not agenda:
        print("\nNenhum contato cadastrado.")
        return
    
    nome = input("\nInsira o nome do contato a remover: ").strip().lower()
    
    if nome in agenda:
        del agenda[nome]
        print(f"\nContato '{nome}' removido com sucesso!")
    else:
        print(f"\nContato '{nome}' não encontrado.")

agenda = {}

while True:
    opcao = menu()
    
    if opcao == "1":
        adicionar_contato(agenda)
    elif opcao == "2":
        ver_contatos(agenda)
    elif opcao == "3":
        buscar_contato(agenda)
    elif opcao == "4":
        remover_contato(agenda)
    elif opcao == "5":
        print("\nSaindo da agenda.")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
