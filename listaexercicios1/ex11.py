def verificar_string(lista, string):
    if string in lista:
        return True
    else:
        return False


entrada_lista = input("\nInsira os itens da lista (separados por vírgula): ")
lista = [item.strip() for item in entrada_lista.split(',')]

string = input("Insira uma string: ")

resultado = verificar_string(lista, string)

print(f"Lista: {lista}")
print(f"Buscando por: '{string}'")
print(f"Está na lista? {resultado}")

if resultado:
    print("A string está na lista")
else:
    print("A string não está na lista")

