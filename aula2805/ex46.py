def soma(n):
    if n == 1:
        return 1
    return 1/n + soma(n+1)

n = int(input("Insira um número n: "))

if n >= 1:
    resultado = soma(n)
    print(f"A soma dos {n} primeiros números da soma harmônica é {resultado:.6f}")
else:
    print("Insira apenas números positivos")
