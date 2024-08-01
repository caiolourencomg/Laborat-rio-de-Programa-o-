# função sem parametros e sem retorno

def boas_vindas():
    print("-----------------INICIO-----------------")



# função sem parametros e com retorno

def calcula_salario(horas_dia, dias_trabalhados, valor_hora = 88.5):
    valor_hora = 88.50
    salario = valor_hora*horas_dia*dias_trabalhados
    return salario
def ler_horas_dia():
    dias_horas = float(input("Digite a quantidade de horas trabalhadas por dias: "))
    return ler_horas_dia

if __name__ == "__main__":
    horas = ler_horas_dia()
    a = calcula_salario (horas,18)
    b = calcula_salario (3,10)

    print (a)
    print (b)