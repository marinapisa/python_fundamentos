# Exercício 18:
# Crie um programa que solicite ao usuário que insira a quantidade de notas do aluno a serem calculadas.
# Em seguida, peça para o usuário digitar as notas uma por uma. Armazene essas notas em uma lista.
# Calcule a média das notas utilizando um for loop para somar todos os elementos da lista e dividir 
# pela quantidade de notas.  Verifique se a média é maior ou igual a 6.0. Se a média for maior ou igual a 6.0, 
# exiba a mensagem "Aluno Aprovado!". Caso contrário, exiba a mensagem "Aluno Reprovado!".

# Dicas:
# Utilize um for loop para solicitar as notas e armazená-las na lista.
# Use um acumulador para calcular a soma das notas e, ao final do loop, divida pela quantidade de notas para obter
#  a média.  Use uma estrutura condicional (if-else) para verificar se o aluno foi aprovado ou reprovado com base 
# na média calculada. Certifique-se de converter os valores digitados pelo usuário para o tipo 
# adequado (int ou float) ao armazená-los na lista.

import os

def ler_quantidade_notas():
    while True:
        try:
            quantidade_notas = int(input('Informe a quantidade de notas: '))
            if quantidade_notas > 0:
                return quantidade_notas
            else:
                # forçando erro:
                raise ValueError('Informe números acima de 0')
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            print('Informe uma quantidadede de notas válidas!')

def ler_notas(quantidade_notas):
    lista_notas = []
    while len(lista_notas) < quantidade_notas:
        try:
            nota = float(input(f'Informe a {len(lista_notas)+1}ª nota: '))
            if nota >= 0  and nota <= 10:
                lista_notas.append(nota)

        except:
            print('Informe uma nota válida!')

    return lista_notas


def calcula_media():
    ...

def verificar_media():
    ...

def script():
  quantidade_notas = ler_quantidade_notas()
  lista_notas = ler_notas(quantidade_notas)
  print('lista: ' , lista_notas)
  
  


if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    script()