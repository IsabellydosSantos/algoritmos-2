# Programa para encontrar caracteres comuns entre duas strings

string1 = input("\nDigite a primeira string: ")
string2 = input("Digite a segunda string: ")

comuns = []
for char in string1:
    if char in string2 and char not in comuns:
        comuns.append(char)

string_comum = ''.join(comuns)

print(f"Caracteres comuns: {string_comum}")
print(f"Quantidade de caracteres comuns: {len(string_comum)}")

