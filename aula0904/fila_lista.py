# Simulacao de uma fila usando lista

# Criando a fila
fila = []

# Inserindo clientes (enqueue)
fila.append("Cliente 1")
fila.append("Cliente 2")
fila.append("Cliente 3")
fila.append("Cliente 4")

print("Fila inicial: ", fila)

# Atendendo clientes (dequeue)
print("\nAtendendo clientes: ")

while fila:  # Enquanto a fila nao estiver vazia
    cliente = fila.pop(0)  # Remove o primeiro elemento
    print(f" Atendido : { cliente }")

print("\nFila vazia: ", fila)

