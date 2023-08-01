# # exercicio 2
# 	Escreva uma função que calcule a média de três notas fornecidas pelo usuário e
# 	armazene o resultado em uma variável. Em seguida, exiba a média calculada no terminal.

import os

def obter_notas():
    soma_notas = 0
    i = 0
    while i < 3:
        try:
            nota = input(f'Informe a {i + 1}ª nota: ')
            nota = float(nota)
            i += 1
            soma_notas += nota
        except:
            print('Informe notas válidas!')
   
    media_notas = soma_notas / 3
    media_arredondada = round (media_notas, 2)
    print(f'A média das notas informadas é: {media_arredondada}') 
        


def calcula_media():
    primeiro_num = int(input('Digite a primeiro nota: '))
    segundo_num = int(input('Digite a segunda nota: '))
    terceiro_num = int(input('Digite a terceira nota: '))
    media_nota = (primeiro_num + segundo_num + terceiro_num) / 3
    print(f'A média das notas informadas é: {media_nota}!')


# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    # calcula_media()
    obter_notas()