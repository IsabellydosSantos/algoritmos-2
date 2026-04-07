import math

def soma(n):
    if n <= 0:
        raise ValueError("O número deve ser maior que 0")

    fatorial = math.factorial(2*n)
    soma_cubos = sum(i**3 for i in range(1, n+1))
    soma_quartas = sum(i**4 for i in range(1, n+1))
    return fatorial + 3*soma_cubos + 4*soma_quartas

try:
    n = int(input("Insira um número inteiro positivo: "))
    resultado = soma(n)
    print(f"Soma: {resultado}")
except ValueError:
    print("Insira apenas números inteiros")