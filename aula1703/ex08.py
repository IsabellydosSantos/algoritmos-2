def mdc(a, b):
    # Troca automática se necessário (sempre a >= b)
    if a < b:
        a, b = b, a  # Troca os valores

    while b != 0:
        resto = a % b
        a, b = b, resto

    return a


def mmc(a, b):
    mdc_valor = mdc(a, b)

    return (a * b) // mdc_valor


n1 = int(input("Insira o primeiro número inteiro positivo: "))
n2 = int(input("Insira o segundoo número inteiro positivo: "))

if n1 < 0 or n2 < 0:
    print("Digite apenas números positivos")


resultadomdc = mdc(n1, n2)
resultadommc = mmc(n1, n2)

print(f"MDC({n1},{n2})")
print(resultadomdc)

print(f"MMC({n1},{n2})")
print(resultadommc)




