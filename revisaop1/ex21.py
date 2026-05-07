def num_tri(n):
    if n < 0:
        return False, None
    elif n == 0:
        return True, (0, 1, 2)

    i = 0
    while i * (i + 1) * (i + 2) <= n:
        if i * (i + 1) * (i + 2) == n:
            return True, (i, i + 1, i + 2)
        i += 1
    return False, None



try:
    n = int(input("Insira um número inteiro positivo: "))

    if n < 0:
        print("Digite apenas números positivos")

    resultado, numeros = num_tri(n)

    print(f"Retorno da função: {resultado}")

    if resultado:
            print(f"O número {n} é triangular e é formado por {numeros[0]} * {numeros[1]} * {numeros[2]}")
    else:
            print(f"O número {n} não é triangular")

except ValueError:
    print("Digite apenas números inteiros")

