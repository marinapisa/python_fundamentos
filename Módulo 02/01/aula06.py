from aula05 import soma, subtracao, multiplicacao, divisao

def menu():
    var = 1
    while var != 0:
        print('Digite qual operação matemática você deseja fazer: ')

        cond = int(input('digite\n1 para Soma\n2 para Subtração\n3 para Multiplicação\n4 para Divisão '))

        match(cond):
            case 1:
                n1 = float(input('Digite o 1º número: '))
                n2 = float(input('Digite o 2º número: '))
                print(soma(n1, n2))
            case 2:
                n1 = float(input('Digite o 1º número: '))
                n2 = float(input('Digite o 2º número: '))
                print(subtracao(n1, n2))
            case 3:
                n1 = float(input('Digite o 1º número: '))
                n2 = float(input('Digite o 2º número: '))
                print(multiplicacao(n1, n2))
            case 4:
                n1 = float(input('Digite o 1º número: '))
                n2 = float(input('Digite o 2º número: '))
                divisao(n1, n2)

        var = int(input('Digite 1 para continuar'))

        #  diferença entre case e if: deve ser usado case quando o caminhos possiveis ja estão premeditados, o if nao se tem controle sobre os dados.

        


