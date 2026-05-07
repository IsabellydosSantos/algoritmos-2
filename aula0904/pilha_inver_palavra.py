# Invertendo uma palavra usando pilha

# Entrada do usuário
palavra = input("Digite uma palavra: ")

# Criando a pilha
pilha = []

# Empilhando os caracteres
for letra in palavra:
    pilha.append(letra)

# Desempilhando para inverter
palavra_invertida = ""

while pilha:
    palavra_invertida += pilha.pop()

print("Palavra invertida: ", palavra_invertida)

