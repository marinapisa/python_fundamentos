# 2 - Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
#     implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
#     que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
#     Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
#     Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
#     como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
#     classes com informações distintas, invoque os métodos e printe o resultado das
#     operações. 


from abc import ABC, abstractmethod

# CLASSE ABSTRATA (MODELO)
class Banco(ABC):
    def __init__(self, nome, saldo, numero_conta):
        self.nome = nome
        self.__saldo = saldo
        self.numero_conta = numero_conta

    @abstractmethod #quando tiver @ é decoradores
    def depositar(self):
        pass

    @abstractmethod
    def ver_saldo(self):
        pass

    @abstractmethod
    def sacar(self):
        pass

    # @abstractmethod
    # def exibir_informacoes(self):
    #     pass




    

# subclasses:

class ContaCorrente(Banco):
    def depositar(self, deposito):
        if deposito > 0:
            self._Banco__saldo += deposito
            print('Deposito realizado com sucesso!')
        else:
            print('Informe um valor acima de zero.')

    def ver_saldo(self):
        return self._Banco__saldo

    def sacar (self, valor_saque):
        self._Banco__saldo -= valor_saque
        print(f'Saque de R${valor_saque} realizado com sucesso!')

    # def exibir_informacoes(self):
    #     print(f'\nNome {self.nome}')
    #     print(f'\nSaldo {self.saldo}')
    #     print(f'\n Numero da conta:  {self.numero_conta}')

        

class ContaPoupanca(Banco):
    def depositar(self, deposito):
        if deposito > 0:
            self._Banco__saldo += deposito
            print('Deposito realizado com sucesso!')
        else:
            print('Informe um valor acima de zero.')
    
    def ver_saldo(self):
        return self._Banco__saldo
    
    def sacar (self):
        print('Não é permitido saque na conta poupança!')

    # def exibir_informacoes(self):
    #     print(f'\nNome: {self.nome}')
    #     print(f'\nSaldo: {self.saldo}')
    #     print(f'\n Numero da conta:  {self.numero_conta}')



if __name__ == '__main__':

    conta1 = ContaPoupanca('Rodrigo', 500, 66666)
    print(conta1.nome)
    print(conta1.ver_saldo())
    conta1.sacar()
    print(conta1.ver_saldo())
    conta1.depositar(100)
    print(conta1.ver_saldo())

    conta2 = ContaCorrente('Adrian', 6000, 99999)
    print(conta2.ver_saldo())
    conta2.sacar(2000)
    print(conta2.ver_saldo())
    conta2.depositar(10000)
    print(conta2.ver_saldo())




    # cooperado1 = ContaCorrente(
    #     nome ='Marina',
    #     saldo = 5000,
    #     numero_conta = 666
    #     )

    # cooperado1.exibir_informacoes()
    # cooperado1.saldo()
    # cooperado1.depositar(100)
    # cooperado1.saldo()
    # cooperado1.sacar(500)
    # cooperado1.saldo()