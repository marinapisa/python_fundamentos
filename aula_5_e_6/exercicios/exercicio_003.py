# 3 - Crie uma classe base Veiculo com atributos como marca, modelo e métodos como ligar()
#     e desligar(), entre outros. Crie as subclasses Carro e Moto que herdam de Veiculo e
#     implementam seus próprios métodos beaseando-se na abstratação de Veiculo. Em seguida,
#     crie uma classe Garagem que aceita veículos e gerencia o estacionamento usando herança.
#     Crie e trabalhe com os getters e setters para a classe Garagem.

from abc import ABC, abstractmethod

# CLASSE ABSTRATA (MODELO)
class Veiculo(ABC):
     def __init__(self, marca, modelo, ligado):
         self.marca = marca
         self.modelo = modelo
         self.ligado = ligado
        

     @abstractmethod #quando tiver @ é decoradores
     def ligar(self):
        pass

     @abstractmethod
     def desligar(self):
        pass
     
# SUBCLASSES
class Carro(Veiculo):
    def ligar(self):
        if self.ligado is True:
            print('O carro ja esta ligado!')
        else:
            self.ligado = True
            print('Carro ligado com sucesso!')

    def desligar(self):
        if self.ligado is False:
            print('O carro ja esta desligado!')
        else:
            self.ligado = False
            print('Carro desligado com sucesso!')


class Moto(Veiculo):
    def ligar(self):
        if self.ligado is True:
            print('A moto ja esta ligada!')
        else:
            self.ligado = True
            print('Moto ligada com sucesso!')

    def desligar(self):
        if self.ligado is False:
            print('A moto ja esta desligada!')
        else:
            self.ligado = False
            print('Moto desligada com sucesso!')


class Garagem:
    def __init__(self):
         self.veiculos_estacionados = []

    def estacionar(self, auto_nome):
        self.veiculos_estacionados.append(auto_nome)
        print(f'Veiculo {auto_nome} estacionado com sucesso')

    def mostra_auto_estacionados(self):
        if len(self.veiculos_estacionados) > 0:
            print('Garagem: ')
            for indice, veiculo in enumerate(self.veiculos_estacionados):
                print(f'Veiculo {indice + 1}: {veiculo}')
        else:
            print('Ainda não existem veículos na garagem!')




if __name__ == '__main__':

    moto_objeto = Moto('Honda', 'Hornet', False)
    carro_objeto = Carro('Fiat', 'Palio', False)

    print(moto_objeto.marca)
    print(moto_objeto.modelo)
    moto_objeto.desligar()
    moto_objeto.ligar()
    moto_objeto.desligar()

    print('\n')

    print(carro_objeto.marca)
    print(carro_objeto.modelo)
    carro_objeto.desligar()
    carro_objeto.ligar()
    carro_objeto.desligar()

    print('\n')
    

    garagem_objeto = Garagem()
    garagem_objeto.mostra_auto_estacionados()

    print('\n')

    garagem_objeto.estacionar(f'Carro da mãe: {carro_objeto.marca}')
    garagem_objeto.estacionar(f'Carro do pai: {carro_objeto.marca}')


    garagem_objeto.estacionar(f'Moto de casa: {moto_objeto.marca}')
    garagem_objeto.estacionar(f'Moto da empresa: {moto_objeto.marca}')

    print('\n')

    garagem_objeto.mostra_auto_estacionados()
