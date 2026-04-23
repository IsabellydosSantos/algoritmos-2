def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mdc_lista(numeros):
    if len(numeros) == 1:
        return numeros[0]
    return mdc(numeros[0], mdc_lista(numeros[1:]))


def mmc(a, b):
    return abs(a * b) // mdc(a,b)


def mmc_lista(numeros):
    if len(numeros) == 1:
        return numeros[0]
    return mmc(numeros[0], mmc_lista(numeros[1:]))


numeros = input("Insira dois ou mais números inteiros positivos (separados por vígula): ")
numeros_str = numeros.split(',')

try:
    numeros = [int(num) for num in numeros_str]

    if len(numeros) < 2:
        print("São necessários ao menos dois números.")

    mdc_resultado = mdc_lista(numeros)
    print(f"MDC: {mdc_resultado}")

    mmc_resultado = mmc_lista(numeros)
    print(f"MDC: {mmc_resultado}")
except ValueError:
    print("Insira apenas números inteiros.")
