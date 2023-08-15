# 3- - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria, com os atributos saldo (private), titular (public), numero_conta (private). Crie métodos get_saldo() e
# set_saldo(novo_saldo) para acessar e modificar o saldo.


class ContaBancaria:
    def __init__(self, saldo, titular, numero_conta):
        self.__saldo = saldo
        self.titular = titular
        self.__numero_conta = numero_conta

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo_novo):
        self.__saldo = saldo_novo

   
        
if __name__ =='__main__':
    conta1 = ContaBancaria(100,'Bruno', 15)
    conta2 = ContaBancaria(300,'Bruna', 16)

    print(conta1.titular)
    print(f'Saldo: {conta1.saldo}')

    print(conta2.titular)
    print(f'Saldo: {conta2.saldo}')

    print('\n')

    conta1.saldo = 500
    conta2.saldo = 900
    # se ele nao fosse privado ele receberia os valores assim: conta1.get_saldo(500)

    print(conta1.titular)
    print(f'Saldo: {conta1.saldo}')

    print(conta2.titular)
    print(f'Saldo: {conta2.saldo}')