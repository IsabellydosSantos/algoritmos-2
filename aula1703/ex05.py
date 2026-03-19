import random

def embaralhar(string):
    caracteres = list(string)
    random.shuffle(caracteres)
    return ''.join(caracteres)


strings = input("Informe uma string: ").lower().strip()

resultado = embaralhar(strings)

print(f"String com caracteres embaralhados: {resultado}")
