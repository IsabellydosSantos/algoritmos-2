def tribonacci(n):
    if n <= 0:
        return []
    seq = [1, 1, 2]
    if n == 3:
        return seq[:n]

    for i in range(3, n):
        prox = seq[i-3] + seq[i-2] + seq[i-1]
        seq.append(prox)

    return seq


n = int(input("Insira um número inteiro positivo: "))

resultado = tribonacci(n)

print(f"Os {n} primeiros números de Tribonacci são: {resultado}")
