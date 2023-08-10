# 3 - Classe Carro:
# Crie uma classe chamada Carro que simule um carro. A classe deve ter os atributos marca, modelo e ano.
# Crie métodos para ligar (ligar()), desligar (desligar()) e exibir as informações do carro (exibir_informacoes()).

class Carro:
    marca = 'Renault'
    modelo = 'Logan'
    ano = 2009

    def ligar():
        print('O carro ligou!')

    def desligar():
        print('O carro desligou!')

    def exibir_informacoes():
        print(f'Este carro é do ano {Carro.ano}, marca {Carro.marca}, modelo {Carro.modelo}')


while True:
    metodo = input('Informe o nome do método: ')
    if metodo.lower() == 'ligar':
        Carro.ligar()
    elif metodo.lower() == 'desligar':
        Carro.desligar()
    elif metodo.lower() == 'exibir':
        Carro.exibir_informacoes()
    elif metodo.lower() == 's':
        print('Programa encerrado')
        break