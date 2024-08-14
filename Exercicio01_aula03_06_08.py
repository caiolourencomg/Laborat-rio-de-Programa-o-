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
# Ojetivo:| 
# Implementar uma função que busque um elemento em uma lista.
# """""""

def busca_elementos(elemento, lista):
    # retornar true caso elemento esteja na lista
    # retornar false caso elemento não esteja na lista
    for numero in lista:
        if elemento == numero:
            return True
    # percorremos toda a lista e não encontramos o elemento
    return False

listao = [3,8,5,4]
numeroaserencotrado = int(input("Digite elemento: "))
if busca_elementos(numeroaserencotrado, listao) == True:
    print(f"{numeroaserencotrado} está na Lista!")
else:
    print(f"{numeroaserencotrado} não está na Lista!")


## Exercicio 3: Função de Contagem de Vogais
# """""""
# Ojetivo:
# Implementar uma função que conte o número de vogais em uma string.
# """""""

def contagem_vogais(nome):
    vogais = "a" , "e" , "i" , "o", "u", "A", "E", "I", "O", "U" 
    soma = 0
    for letras in vogais:
        soma +=1
    return soma

nome = input("Digite seu nome aqui para sabermos quantas vogais ele contem:" )
total_de_vogais = contagem_vogais(nome)
print(f"Número de vogais no nome '{nome}': {total_de_vogais}")