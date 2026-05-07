def calc(dias,km):
    aluguel = dias * 60
    kmt = km * 0.15
    total = aluguel + kmt

    return total


dias = float(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos KMs foram percorridos? "))

resultado = calc(dias,km)

print(f"O preço total a ser gasto é de R${resultado}")

