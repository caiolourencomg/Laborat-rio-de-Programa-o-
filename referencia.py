def passagem_referencia(x):
    x[3] = 2
    print("dentro passagem_referencia")
    print(x)

lista = [10,20,30,40,50]
print("antes passagem_referencia")
print(lista)
passagem_referencia(lista)
print("depois passagem referencia")
print(lista)