import random

n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
n5 = input('Digite um nome: ')

lista = [n1, n2, n3, n4, n5]

print(lista)

sorteio = random.choice(lista)

print (sorteio)