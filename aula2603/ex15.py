def n_pares(n):
    if n < 0:
        return []

    lista = n_pares(n-1)

    if n % 2 == 0:
        lista.append(n)
    return lista


try:
    n = int(input("Insira um número inteiro positivo par: "))

    if n <= 0:
        print("Insira apenas números positivos.")

    resultado = n_pares(n)

    print(f"0s números pares de 0 até {n} são: {resultado}")

except ValueError:
    print("Insira apenas números inteiros.")
    
