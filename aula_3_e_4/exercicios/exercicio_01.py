# 1 - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria que simule uma conta bancária simples.
# A classe deve ter os atributos titular, saldo e numero. Crie métodos para depositar (depositar(valor))
# e sacar (sacar(valor)) dinheiro da conta, além de um método para exibir o saldo atual (exibir_saldo()).

class ContaBancaria:
    titular = 'Marina'
    saldo = 0
    numero = 666

    def deposita(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo += valor
        except:
            print('Informe um valor válido para depósito!')

    def saca(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo -= valor
        except:
            print('Informe um valor válido para saque!')
    
    def exibir_saldo():
        print(f'Titular {ContaBancaria.titular} com conta {ContaBancaria.numero} tem saldo R${ContaBancaria.saldo}')

    def script():
        while True:
            try:
                opcao = input('\nInforme \n1 para depositar \n2 para sacar \n3 para exibir \n4 para sair: ')
                if opcao == '1':
                    valor = input('Informe o valor: ')
                    ContaBancaria.deposita(valor)
                elif opcao == '2':
                    valor = input('Informe o valor: ')
                    ContaBancaria.saca(valor)
                elif opcao == '3':
                    ContaBancaria.exibir_saldo() 
                elif opcao == '4':
                    print('Volte sempre com dinheiro!!')
                    break
            except:
                print('Informe uma opção Válida!')

if __name__ == '__main__':
    ContaBancaria.script()