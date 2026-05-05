try:
    arquivo = open("notas.txt", "r")

    for linha in arquivo:
        linha = linha.strip()

        parte = linha.split()
        nome = parte[0]

        notas = []
        for i in range(1, len(parte)):
            notas.append(float(parte[i]))

        if len(notas) > 6:
            media = sum(notas)/len(notas)
            print(f"Estudante: {nome}\nMédia: {media:.2f}")
except:
    print("Não foi possível abrir o arquivo.")

