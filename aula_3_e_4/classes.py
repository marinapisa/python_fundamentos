# nome_usuario = 'caue'  snake case
# NomeUsuario = 'caue' camel case

class ClasseCachorro:
    raca = 'Pit Bull'
    idade = 3

    def latir(latidas):
        for latida in range(latidas):
            print('au au')

    def comer(comida, horario):
        print(f'au au, comi {comida}, au au em horario {horario}')

    def mostrar_info_dog():
        print(f'O cachorro é da raça {ClasseCachorro.raca} e tem {ClasseCachorro.idade} anos')




class ClassePessoa:
    # atributos = variaveis
    nome  = 'Marina'
    idade = 28
    altura = 1.69
    peso  = 82
    pais_origem  = 'Brasil'
    genero = 'Feminino'

    # métodos = funções
    def dizer_ola():
        print(f'Olá, eu sou {ClassePessoa.nome}')

    def mostrar_dados():
        print(f'Eu tenho {ClassePessoa.idade} anos, {ClassePessoa.altura} de altura, ' +
              f'{ClassePessoa.peso} kilos e meu genero é {ClassePessoa.genero}')

    def mostrar_origem():
        print (f'Eu venho do {ClassePessoa.pais_origem}!')

ClasseCachorro.latir(10)
ClasseCachorro.comer('ração', '10h')
ClasseCachorro.mostrar_info_dog()

ClassePessoa.dizer_ola()
ClassePessoa.mostrar_dados()
ClassePessoa.mostrar_origem()