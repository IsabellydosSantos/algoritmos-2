# Programa para encontrar caracteres comuns entre duas strings

print("=" * 50)
print("ENCONTRADOR DE CARACTERES COMUNS")
print("=" * 50)

# Receber as duas strings
string1 = input("\nDigite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Encontrar caracteres comuns (sem repetir)
comuns = []
for char in string1:
    if char in string2 and char not in comuns:
        comuns.append(char)

# Converter para string
string_comum = ''.join(comuns)

# Exibir resultados
print("\n" + "=" * 50)
print("RESULTADOS")
print("=" * 50)
print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Caracteres comuns: {string_comum}")
print(f"Quantidade de caracteres comuns: {len(string_comum)}")
