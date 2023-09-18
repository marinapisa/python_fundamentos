def sobrenome():
    sobrenome = input('Digite seu sobrenome: ')
    return sobrenome

def idade():
    idade = int(input('Digite sua idade: '))
    return idade

def nome():
    nome = input('Digite seu nome: ')
    return nome

def cpf():
    cpf = input('Digite seu CPF: ')
    return cpf

a = nome()
b = sobrenome()
c = idade()
d = cpf()

print(f'Nome {a}, Sobrenome {b}, idade {c} CPF {d}')