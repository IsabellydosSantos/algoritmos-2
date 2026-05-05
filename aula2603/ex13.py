def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)


try:
    n = int(input("Insira um número inteiro positivo: "))

    if n <= 0:
        print("Insira apenas números positivos.")

    resultado = soma(n)

    print("O resultado do somátorio dos números é: ", resultado)

except ValueError:
    print("Insira apenas números inteiros.")

