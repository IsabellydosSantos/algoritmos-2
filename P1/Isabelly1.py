def soma(n):
    if n <= 0:
        return 0

    soma = 0
    for i in range(1,n+1):
        soma += (n-i+1) / i

    return soma


try:
    n = int(input("Insira um número inteiro positivo: "))

    if n <= 0:
        print("Insira apenas números positivos.")
    else:
        resultado = soma(n)
        print(f"A soma de {n} é igual a: {resultado}")
except ValueError:
    print("Insira apenas números inteiros")
