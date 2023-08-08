class Calculator:
    operacoes_limite = 10
    input_mensagem = 'Informe um número entre 1 e 5: '
    input_mensagem += '\n1 = somar'
    input_mensagem += '\n2 = subtrair'
    input_mensagem += '\n3 = multiplicar'
    input_mensagem += '\n4 = dividir'
    input_mensagem += '\n5 = módulo'
    input_mensagem += '\nInforme a operação:'

    def somar(numero_um, numero_dois):
        print(f'\33[032m  A soma dos números é: {numero_um + numero_dois}\33[0m')

    def subtrair(numero_um, numero_dois):
        print(f'\33[032m  A subtração dos números é: {numero_um - numero_dois}\33[0m')

    def multiplicar(numero_um, numero_dois):
        print(f'\33[032m  A multiplicação dos números é: {numero_um * numero_dois}\33[0m')

    def dividir(numero_um, numero_dois):
        print(f'\33[032m  A divisão dos números é: {numero_um / numero_dois}\33[0m')

    def modulo(numero_um, numero_dois):
        print(f'\33[032m  A sobra da divisão dos números é: {numero_um % numero_dois}\33[0m')

    def controle_operacoes():
        contador = 0
        while contador < Calculator.operacoes_limite:
            contador += 1
            try:
                print(f'\nOperação {contador}')
                numero_um = int(input('Informe o primeiro número: '))
                numero_dois = int(input('Informe o segundo número: '))

                if numero_um > 0 and numero_dois > 0:
                    while True:
                        try:
                            opcao = int(input(Calculator.input_mensagem))

                            if opcao == 1:
                                Calculator.somar(numero_um, numero_dois)
                                break
                            elif opcao == 2:
                                Calculator.subtrair(numero_um, numero_dois)
                                break
                            elif opcao == 3:
                                Calculator.multiplicar(numero_um, numero_dois)
                                break
                            elif opcao == 4:
                                Calculator.dividir(numero_um, numero_dois)
                                break
                            elif opcao == 5:
                                Calculator.modulo(numero_um, numero_dois)
                                break
                            else:
                                raise ValueError()
                            
                        except:
                            print('Informe uma opção valida!')
                else:
                    print('Informe números maiores que Zero.')
            except KeyboardInterrupt:
                print('\nPrograma encerrado manualmente ctrl c')
                quit()
            except:
                print('Informe números válidos!')

if __name__ == '__main__':
    Calculator.controle_operacoes()