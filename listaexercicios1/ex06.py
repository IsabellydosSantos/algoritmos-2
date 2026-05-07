print("Insira apenas números inteiros. Digite 0 para encerrar")

soma = 0
contador = 0

while True:
  try:
    n = float(input("Digite um número: "))

    if n == 0:
      break

    soma += n
    contador += 1

  except ValueError:
    print("Digite apenas números inteiros")
    
if contador > 0:
  media = soma/contador
  print(f"Quantidade total de números: {contador}")
  print(f"Soma total: {soma:.2f}")
  print(f"Média Aritmética: {media:.2f}")
else:
  print("Nenhum número foi digitado antes do 0")

