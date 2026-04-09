vel = float(input("Qual a velocidade do carro (em KM)? "))

if vel > 80:
    kma = vel - 80
    multa = 5 * kma
    print(f"Você foi multado, o valor da multa é de RS{multa}")
