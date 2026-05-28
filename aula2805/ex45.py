def soma_div(n):
    soma = 0
    for i in range(1,n):
        if n % i == 0:
            soma += i
    return soma


def n_amigo(a,b):
    return soma_div(a) == b and soma_div(b) == a

a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))

if n_amigo(a,b):
    print(f"{a} e {b} são números amigos")
else:
    print(f"{a} e {b} não são números amigos")
