def fat_duplo(n):
    if n <= 1:
        return 1

    return n * fat_duplo(n-2)


try:
    n = int(input("Insira um número inteiro positivo: "))

    if n <= 0:
        print("Insira apenas números positivos.")

    resultado = fat_duplo(n)

    print("O resultado do fatorial duplo é: ", resultado)

except ValueError:
    print("Insira apenas números inteiros.")
