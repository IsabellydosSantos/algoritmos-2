import pickle
try:
    arquivo = open("teste.bin", "wb")
    lista = [1, 2, 3]
    pickle.dump(lista, arquivo)
    print(lista)
    arquivo.close()
except:
    print("Problemas com o arquivo.")