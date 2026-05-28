def unir():
    try:
        c1 = set(map(int,input("Insira os elementos do 1° conjunto(separados por espaço): ").split()))
        c2 = set(map(int, input("Insira os elementos do 2° conjunto(separados por espaço): ").split()))
    except ValueError:
        print("Insira apenas números")
        return

    uniao = c1 | c2

    print(f"União dos conjuntos A e B: {sorted(uniao)}")
