# Exercício 19:
# Escrever uma função que solicita ao usuário uma senha e verifica se ela atende a alguns critérios de segurança.
# Usar laço de repetição para rodar até uma senha válida ser informada e a mesma ser informada duas vezes de
# forma identica para confirmação da senha.
# Critérios de segurança:
# A senha deve conter pelo menos 8 caracteres.
# A senha deve conter pelo menos uma letra maiúscula e uma letra minúscula.
# A senha deve conter pelo menos um número.
import os


lista_letras_minusculas =  [
    'a', 'b', 'c', 'd', 'e', 'f'
    'g', 'h', 'i', 'j' 'k', 'l', 'm'
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

lista_letras_maiúsculas =  [
    'A', 'B', 'C', 'D', 'E', 'F'
    'G', 'H', 'I', 'J' 'K', 'L', 'M'
    'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

lista_numeros = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']


def solicita_senha_valida():
    senha_valida = False
    while senha_valida is False:
        senha_temporaria = input('Informe a senha: ')
        
        validou_caracteres = False
        validou_letras = False
        validou_numero = False

        # valida tamanho da senha
        if len(senha_temporaria) >= 8:
            validou_caracteres = True

        # variaveis para validar maiusculas/minusculas
        maiuscula_apareceu= False
        minuscula_apareceu = False

        # transforma senha em lista
        lista_chars = list(senha_temporaria)

        # verifica se cada letra da senha aparece nas listas de letras maiuscuuas e minusculas
        for letra in lista_chars:
            if letra in lista_letras_minusculas:
                minuscula_apareceu = True
            elif letra in lista_letras_maiúsculas:
                maiuscula_apareceu = True


        # verifica se achou tanto uma maiuscula como uma minuscula
        if maiuscula_apareceu is True and minuscula_apareceu is True:
            validou_letras = True

        # verificar se aparece numero na senha informada
        for char in lista_chars:
            if char in lista_numeros:
                validou_numero = True
                break

        if validou_numero is True and validou_letras is True and validou_caracteres is True:
            ...
        else:
            print(f'Tem pelo menos 8 caracteres: {validou_caracteres}')
            print(f'Tem letra maiuscula/minuscula: {validou_letras}')
            print(f'Tem pelo menos um numero: {validou_numero}')


        







def main():
   ...

if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    main()