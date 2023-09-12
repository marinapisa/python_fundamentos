# if e else > utiliza de operadores relacionais para exibir ou executar o código
# switch Case > que definida que entra em uma estrutura de caso

# For > é uma estrutura de repetição que é composta por indices
#  While > é o filho do if e do for, por que é uma estrutura de reetição que é baseada em operadores relacionais

# chave a valor 

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))
# procedencia aritmética
media =  (nota1 + nota2) / 2

aluno = {
  'Nome >>' : nome,
  'Idade >>': idade,
  'Nota 1 >>' : nota1,
  'Nota 2 >>' : nota2,
  'Media >>' : media
 }

cond = int (input(
    ''' Digite o numero que representa a caracteristica que deseja saber
    \n1 - Nome
    \n2 - Idade
    \n3 - Primeira nota
    \n4 - Segunda nota
    \n5 - Média
    \n >>>>> '''
))

if cond == 1:
    print(f'O nome do aluno é {aluno ["Nome >>"]}')
elif cond ==2:
    print(f'A idade do aluno é {aluno["Idade >>"]}')
elif cond ==3:
    print(f'A primeira nota do aluno é {aluno["Nota 1 >>"]}')
elif cond ==4:
    print(f'A segunda nota do aluno é {aluno["Nota 2 >>"]}')
elif cond ==5:
    print(f'A media das notas do aluno é {aluno["Media >>"]}')
else:
    print('Digite um valor válido!')