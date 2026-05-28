c1 = set(map(int, input("Insira os elementos do primeiro conjunto (separados por espaço): ").split()))
c2 = set(map(int, input("Insira os elementos do segundo conjunto (separados por espaço): ").split()))

inter = c1 & c2

print("Resultado: ", *sorted(inter))
