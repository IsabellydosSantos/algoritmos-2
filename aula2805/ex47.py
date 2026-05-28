senhac = "SEQTS"
tentativas = 0

while tentativas < 3:
    senha = input("Insira a senha: ")
    if senha == senhac:
        print("Acesso liberado")
        break
    else:
        tentativas += 1
        if tentativas == 3:
            print("Senha bloqueada. Favor procurar a administração")
        else:
            print("Senha inválida. Tente novamente")
