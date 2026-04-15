def verificar_string(lista, string):
    """
    Verifica se a string está presente na lista
    Retorna True se estiver, False caso contrário
    """
    if string in lista:
        return True
    else:
        return False

# Programa principal
print("=" * 50)
print("VERIFICADOR DE STRING NA LISTA")
print("=" * 50)

# Receber a lista do usuário
entrada_lista = input("\nDigite os itens da lista (separados por vírgula): ")
lista = [item.strip() for item in entrada_lista.split(',')]

# Receber a string a ser verificada
string_busca = input("Digite a string para buscar: ")

# Chamar a função
resultado = verificar_string(lista, string_busca)

# Exibir resultado
print("\n" + "=" * 50)
print("RESULTADO")
print("=" * 50)
print(f"Lista: {lista}")
print(f"Buscando por: '{string_busca}'")
print(f"Está na lista? {resultado}")

if resultado:
    print("✅ A string foi ENCONTRADA na lista!")
else:
    print("❌ A string NÃO FOI ENCONTRADA na lista!")
