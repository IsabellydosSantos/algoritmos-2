n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))
n3 = int(input("Insira o terceiro número inteiro: "))

if (n1>=n2) and (n1>=n3):
    print(n1)
elif (n2>=n3):
    print(n2)
else:
    print(n3)