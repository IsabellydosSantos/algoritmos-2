def is_palindromo(n):
    # Remove o sinal negativo
    n = abs(n)
    
    # Inverte o número matematicamente
    invertido = 0
    temp = n
    
    while temp > 0:
        invertido = invertido * 10 + (temp % 10)
        temp //= 10
    
    return n == invertido

# Teste rápido
print("Digite um número: ", end="")
num = int(input())

if is_palindromo(num):
    print(f"{num} é palíndromo!")
else:
    print(f"{num} não é palíndromo.")
