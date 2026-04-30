def multiplo():

    try:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))

        if n2 == 0:
            print("Não é possível fazer divisão por 0")

        if n1 % n2 == 0:
            print(f"{n1} é múltiplo de {n2}")
            return True
        else:
            print(f"{n1} não é múltiplo de {n2}")
            return False

    except ValueError:
        print("Insira apenas números válidos")
        return False


multiplo()

