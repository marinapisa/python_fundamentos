# exercicio 3
# Crie uma função que peça ao usuário que digite um número inteiro e, em seguida,
# armazene esse valor em uma variável. Crie mais funções para o usuário também informar 
# dados do tipo float e string, e armazene todos os dados em variáveis. Em seguida
# adicione todos esses items em uma lista e mostre os item através de um laço de repetição for. 

import os

def digite_num():
    num_inteiro = 0 
    num_inteiro = int(input('Digite um número inteiro: '))

def digite_quebrado():
    num_quebrado = 0.0
    num_quebrado = input('Digite um numero quebrado: ')

def digite_str():
    texto = ''
    texto = input('Digite uma palavra: ')

def mostrar_dados():
    lista_inform = []
    num_inteiro = digite_num()
    lista_inform.append(num_inteiro)

    num_quebrado = digite_quebrado()
    lista_inform.append(num_quebrado)

    texto = digite_str()
    lista_inform.append(texto)

    for item in lista_inform:
        print (item)

# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    digite_num()
    digite_quebrado()
    digite_str()
    mostrar_dados()