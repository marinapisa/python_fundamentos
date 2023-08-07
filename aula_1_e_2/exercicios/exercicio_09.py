# Exercício 9:
# Crie uma função que converta um valor em dólar para real. Peça ao usuário que insira a cotação do dólar e o 
# valor em dólar a ser convertido. Em seguida, exiba o valor equivalente em reais.

import os


def converter_valor():
    cotacao = float(input('Informe a cotação do dólar: '))
    valor_dolar = float(input('Informe o valor em Dólar que deseja converter para Real: '))
    conversao = valor_dolar * cotacao
    print(f'O valor convertido em Real é: R${conversao}')


def main():
    converter_valor()


if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    main()