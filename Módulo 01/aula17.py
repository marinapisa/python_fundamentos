from time import sleep

situacao = 'Reprovado'

while situacao =='Reprovado':
# 1º Bloco
    nome = input('digite seu nome: ')
    sobre_nome = input('Digite seu sobrenome: ')
    idade = int(input('digite sua idade:'))
# 2º Bloco
    lista_notas = []
    for lista in range(0, 4):
        nota = float(input('Digite sua nota: '))
        lista_notas.append(nota)
        media = sum(lista_notas) / len(lista_notas)
# 3º Bloco
    if media < 7:
        situacao = 'Reprovado'
        print(f'Infelizmente você foi {situacao} com a média {media}')
    if media >=7:
        for c in range(0,10):
            print('*')
            sleep(1.5)
            situacao = 'Aprovado'
        print(f'Parabéns você foi {situacao} com média {media}!!!!!')
# 4º Bloco
    dicionario = {
        'Nome': nome,
        'SobreNome' : sobre_nome,
        'Idade' : idade,
        'Lista_Notas': lista_notas,
        'Media': media,
        'Situacao' : situacao
    }

    var = input('Você deseja saber um relat[orio completo sobre o aluno? \nSim\nNão')
    if var == 'sim':
        print(f'''{dicionario["Nome"]}
        \n{dicionario["SobreNome"]}
        \n{dicionario["Idade"]}
        \n{dicionario["Lista_Notas"]}
        \n{dicionario["Media"]}
        \n{dicionario["Situacao"]}
''')
    