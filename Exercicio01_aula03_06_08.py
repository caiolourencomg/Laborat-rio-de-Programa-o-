## Exercicio 1: Função de Soma de Elementos
# """""""
# Ojetivo:
# Implementar uma função que calcule a soma dos elementos de uma lista.
# """""""
def soma_elementos(a):
    soma = sum(a)
    return soma

somas = soma_elementos([10,20,30,40,50])
print(somas)    


## Exercicio 2: Função de Busca de Elementos
# """""""
# Ojetivo:
# Implementar uma função que busque um elemento em uma lista.
# """""""

#def busca_elementos(b):



## Exercicio 3: Função de Contagem de Vogais
# """""""
# Ojetivo:
# Implementar uma função que conte o número de vogais em uma string.
# """""""

def contagem_vogais(nome):
    vogais = "a" , "e" , "i" , "o", "u"
    soma = 0
    for letras in vogais:
        soma +=1
    return soma

nome = input("Digite seu nome aqui para sabermos quantas vogais ele contem:" )
total_de_vogais = contagem_vogais(nome)
print(f"Número de vogais no nome '{nome}': {total_de_vogais}")