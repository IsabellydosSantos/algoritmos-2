# soma: -1+2-3+4-5+6-...+n

def soma_alt(n):
    soma = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            soma += i
        else:
            soma -= i
    return soma

try:
    n = int(input("Insira um número inteiro positivo: "))
    resultado = soma_alt(n)
    print(f"Soma: {resultado}")
except ValueError:
    print("Insira apenas números inteiros")
