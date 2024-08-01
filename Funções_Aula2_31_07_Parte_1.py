# função com parametros e sem retorno
def calcula_salario(horas_dia, dias_trabalhados):
    valor_hora = 88.50
    salario = valor_hora*horas_dia*dias_trabalhados
    print(f"R${salario:.2f}")

if __name__ == "__main__":
    calcula_salario (8,18)
    calcula_salario (3,10)