vetor1 = []
print("Insira 10 valores para o primeiro vetor: ")
for i in range(10):
    valor = int(input(f"Vetor 1: {i+1}° Valor: "))
    vetor1.append(valor)

vetor2 = []
print("Insira 10 valores para o segundo vetor: ")
for i in range(10):
    valor = int(input(f"Vetor 2: {i+1}° Valor: "))
    vetor2.append(valor)

vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(f"Vetor 3: {vetor3}")
