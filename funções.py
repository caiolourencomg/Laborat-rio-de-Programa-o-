# Gerador de senhas seguras
"""
Crie uma função chamada gerar_senha que receba 3 parametros opcionais:
-- tamanho (int) - Definir o comprimento da senha a ser gerada.
-- valor padrão deve ser 8.
-- incluir_numeros (boleando) - Define se a senha deve incluir numeros (Entre 0 e 9). O valor padrão deve ser TRUE.
-- incluir_caracteres_especiais (boleando) - Define se a senha deve incluir caracteres especiais ( @, $,#...). O valor padrão deve ser TRUE.

Descrição: a Função ela deve retornar uma str que represente a senha gerada, conforme as especificadas.
Ex: se invocar gerar_senha(incluir_numeros = TRUE, incluir_caracteres_especiais = False) .
--> devolver senha numerica com oito digitos.

Requisitos
1 -  A função não deve gerar senhas com tamanho inferior a 4 caracteres. Caso contrario, retornar uma mensagem: "O tamanho minimo para a senha é de 4 caracteres."
2 - Caso a senha não tenha numeros e nem caracteres especiais ela será composta apenas por letras.
"""
import string
import random

def gerar_senha(tamanho = 8, incluir_numeros = True, inluir_caracteres_especiais = True):
    if tamanho < 4:
        return "O tamanho minimo para a senha é de 4 caracteres!"
    senha = ""
    while len(senha) < tamanho:
        senha = senha + gerar_letras() + gerar_caracteres_especiais() + gerar_numeros()
        
    random.choices(senha, k = tamanho)
    return "".join(senha)
    
def gerar_letras():
    letras = string.ascii_letters
    return random.choice(letras)

def gerar_numeros():
    numeros = string.digits
    return random.choice(numeros)

def gerar_caracteres_especiais():
    caracteres = string.punctuation
    return random.choice(caracteres)

teste01 = gerar_senha(tamanho = 8, incluir_numeros = True, inluir_caracteres_especiais = True)
print(teste01)