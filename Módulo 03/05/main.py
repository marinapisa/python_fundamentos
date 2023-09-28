from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

cond = 0
while cond == 0:
        print('Digite a operação desejada')
        var = input('Digite pf para Pessoa Fisica e pf para Pessoa Jurídica: ')

        match var:

            case 'pf':
                pf = PessoaFisica(
                    input('Digite o nome do Titular: '),
                    input('Digite o CPF do titular: '),
                    float(input('Digite o saldo Inicial: '))
                    )
                print(pf)

                var = input('Você deseja cadastrar o segundo Titular?\nSim\nNão\n>>')
                if var == 'sim':
                    pf.Segundo_Titular = input('Digite o nome do Segundo Titular: ')
                    print(pf)

            case 'pj':
                pj = PessoaJuridica(
                    input('Digite o nome do Titular da PJ: '),
                    input('Digite o CNPJ do titular: '),
                    float(input('Digite o saldo Inicial: '))
                    )
                print(pj)

                var = input('Você deseja cadastrar o segundo Titular?\nSim\nNão\n>>')
                if var == 'sim':
                    pj.Segundo_Titular = input('Digite o nome do Segundo Titular: ')
                    print(pj)

        cond = int(input('Digite 0 para continuar ou 1 para sair:\n'))