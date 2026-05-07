from collections import deque

fila = deque()

fila.append(" Doc1 ")
fila.append(" Doc2 ")
fila.append(" Doc3 ")

while fila:
    print("Imprimindo: ", fila.popleft())

