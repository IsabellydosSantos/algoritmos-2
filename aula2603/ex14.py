def soma_cubo(n):
    if n == 1:
        return 1
    else:
        return n**3 + soma_cubo(n-1)


try:
    n = int(input("Insira um número inteiro positivo: "))

    if n <= 0:
        print("Insira apenas números positivos.")

    resultado = soma_cubo(n)

    print("O resultado do somátorio dos números ao cubo é: ", resultado)

except ValueError:
    print("Insira apenas números inteiros.")
