def potencia(base, exp):
    resultado = 1

    for n in range(1,exp+1):
        resultado *= base

    return resultado