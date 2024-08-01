from Funções_Aula2_31_07_Parte_3 import ler_horas_dia, calcula_salario

h = ler_horas_dia()
salario = calcula_salario(h, 15, 50)

print(f"R${salario:.2f}")