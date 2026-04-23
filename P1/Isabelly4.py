def freq(texto):
    pontuacao = ',.:;?!"'
    texto_rev = ''

    for char in texto:
        if char not in pontuacao:
            texto_rev += char

    palavras = texto_rev.split()

    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    pares_ord = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
    freq_ord = dict(pares_ord)

    return freq_ord


string = input("Insira uma string: ").strip().lower()

resultado = freq(string)

palavra_freq = list(resultado.keys())[0]
quant = list(resultado.values())[0]

print(f"{resultado} sendo a palavra mais frequente {palavra_freq} com quantidade {quant}")
