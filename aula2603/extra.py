def soma_dig(n):
    if n == 0:
        return 0

    return n % 10 + soma_dig(n//10)


try:
    n = int(input("Insira um número inteiro positivo: "))

    if n <= 0:
        print("Insira apenas números positivos.")

    resultado = soma_dig(n)

    print(f"O resultado do somátorio dos dígitos de {n} é: {resultado}")

except ValueError:
    print("Insira apenas números inteiros.")
