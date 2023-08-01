import os


def mostrar_lista():
    lista_dados = [
        1,
        2,
        3,
        'hello',
        'hi',
        False,
        True,
        1.5,
        21,
        'texto!'
    ]

    for item in lista_dados:
        print(item)

def obter_mostrar_dados():
    lista_input = []

    for i in range(5):
        item = input(f'Informe o {i + 1}º item: ')
        lista_input.append(item)

    print('\nItens informados na lista: ')
    for item in lista_input:
        print(item)

# enquanto tiver este, só vai executar o que estiver aq dentro
if __name__ == '__main__':
    os.system ('cls')
    os.system ('python --version')
    # mostrar_lista()
    # obter_mostrar_dados()

    

    