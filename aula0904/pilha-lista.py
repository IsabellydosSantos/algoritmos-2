# Simulacao de uma pilha usando lista

# Criando a pilha
pilha = []

# Inserindo elementos ( push )
pilha.append(10)
pilha.append(20)
pilha.append(30)
pilha.append(40)

print(" Pilha inicial :", pilha)

# Removendo todos os elementos ( pop )
print("\nRemovendo elementos da pilha: ")

while pilha:  # Enquanto a pilha nao estiver vazia
    elemento = pilha.pop()
    print(f" Removido : { elemento } ")

print("\nPilha vazia: ", pilha)
