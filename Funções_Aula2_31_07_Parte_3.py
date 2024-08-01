# função com parametros e com retorno
def calcula_salario(horas_dia, dias_trabalhados, valor_hora = 88.5):
    valor_hora = 88.50
    salario = valor_hora*horas_dia*dias_trabalhados
    return salario

if __name__ == "__main__":
    a = calcula_salario (8,18)
    b = calcula_salario (3,10)

    print (a)
    print (b)