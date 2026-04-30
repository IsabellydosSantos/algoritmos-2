def verificar():

    try:
        n1 = int(input("Insira o primeiro número inteiro positivo: "))
        n2 = int(input("Insira o segundo número inteiro positivo: "))
        n3 = int(input("Insira o terceiro número inteiro positivo: "))

        if n1 + n2 == n3:
            print(f"{n1} + {n2} resulta em {n3}")
        elif n1 + n3 == n2:
            print(f"{n1} + {n3} resulta em {n2}")
        elif n2 + n3 == n1:
            print(f"{n2} + {n3} resulta em {n1}")
        else:
            print("Não há nenhuma combinação de soma que resulte no terceiro número.")

    except ValueError:
        print("Insira apenas números inteiros positivos")
    return False


verificar()

