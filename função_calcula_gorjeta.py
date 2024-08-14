def calcula_gorjeta(valor, porcentual = 10):
    print (f"valor {valor}")
    print (f"porcentual {porcentual}")
    return valor*(porcentual/100)

gorjeta = calcula_gorjeta(400)
print(f"{gorjeta}")
cascai = calcula_gorjeta(400,5)
print(f"{cascai}")
