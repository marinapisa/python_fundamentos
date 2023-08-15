from abc import ABC, abstractmethod

class PessoaAbstrata(ABC):
    @abstractmethod
    def gastar_dinheiro():
        pass

    @abstractmethod
    def respirar():
        pass

    @abstractmethod
    def falar():
        pass


class Atleta(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto pouco dinheiro!')

    def falar():
        print('Queremos um aumento!')
              
    def respirar():
        print('estou respirando profundamente')


class Artista(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto muito dinheiro pq eu posso!')

    def falar():
        print('eu sou rico e falo 5 idiomas')

Artista.gastar_dinheiro()
Atleta.gastar_dinheiro()
Atleta.falar()
Artista.falar()
Atleta.respirar()
Artista.respirar()