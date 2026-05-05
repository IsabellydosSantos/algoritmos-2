def letra(texto):
    if not texto:
        return "String vazia"

    contagem = {}

    for letra in texto:
        if letra.isalpha():
            contagem[letra] = contagem.get(letra, 0) + 1

    letra_freq = max(contagem.values())

    for letra in texto:
        if contagem[letra] == letra_freq:
            return letra


texto = input("Insira uma string: ").strip().lower()

resultado = letra(texto)

print(f"A letra mais comum é: {resultado}")

