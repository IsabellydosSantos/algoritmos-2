def freq(texto):
    pontuacao = '.,:;?!"'
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

    pares_ord = sorted(frequencia.items(), key=lambda x: x[1], reverse=True) #para cada item x pega o elemento na posição 1(quantidade)
    freq_ord = dict(pares_ord)

    return freq_ord


entrada = input("Insira uma string: ").strip().lower()

resultado = freq(entrada)

palavra_freq = list(resultado.keys())[0]
quantidade = list(resultado.values())[0]
print(f"{resultado}\nA palavra mais frequente é '{palavra_freq}' que aparece {quantidade} vezes")

