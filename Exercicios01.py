def fat(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for number in range(1,numero+1):
            resultado *= number
        return resultado
    
def dividir_grupos(total_n, grupos_m):
    possibilidades = fat(total_n)/(fat(grupos_m)*fat(total_n-grupos_m))
    print(possibilidades)
    return possibilidades
    

dividir_grupos(8, 2)
