# 5 - Crie uma classe Alimento com atributos como nome e calorias. Crie subclasses Fruta, Legume
#     e Carne que herdam de Alimento e implementam seus próprios atributos. Crie uma função que aceita 
#     uma lista de alimentos e calcula o total de calorias usando polimorfismo. Para mais precisão no
#     exercício, é ideal pesquisar as calorias dos alimentos e criar objetos das subclasses com seus 
#     respectivos construtores e atributos.



from abc import ABC, abstractmethod

# CLASSE ABSTRATA (MODELO)
class Alimento(ABC):
     def __init__(self, calorias, nome):
         self.calorias = calorias
         self.nome = nome

   
# SUBCLASSES

class Fruta(Alimento):
    pass

class Legume(Alimento):
    pass

class Carne(Alimento):
    pass


def calcular_calorias(lista_caloria):
    soma_calorias = 0 
    for caloria in lista_caloria:
        soma_calorias += caloria

    return soma_calorias




if __name__ == '__main__':

    cenoura = Legume(25, 'cenoura')
    vagem = Legume(30, 'vagem')
    beterraba = Legume(60, 'beterraba')

    lista_legumes = [
        cenoura.calorias,
        vagem.calorias,
        beterraba.calorias        
        ]
    
    calorias_total_legumes = calcular_calorias(lista_legumes)
    print(f'A soma de calorias de {cenoura.nome}', end=' ')
    print(f'{vagem.nome} e {beterraba.nome}', end=' ')
    print(f'é: {calorias_total_legumes}')





    frango = Carne(25, 'File de frango')
    bife = Carne(70, 'Patinho')
    picanha = Carne(120, 'picanha')

    lista_carne = [
        frango.calorias,
        bife.calorias,
        picanha.calorias        
        ]
    
    calorias_total_carne = calcular_calorias(lista_carne)
    print(f'A soma de calorias de {frango.nome}', end=' ')
    print(f'{bife.nome} e {picanha.nome}', end=' ')
    print(f'é: {calorias_total_carne}')




    banana = Fruta(200, 'banana')
    melancia = Fruta(88, 'melancia')
    maracuja = Fruta(50, 'maracuja')

    lista_fruta = [
        banana.calorias,
        melancia.calorias,
        maracuja.calorias        
        ]
    
    calorias_total_fruta = calcular_calorias(lista_fruta)
    print(f'A soma de calorias de {banana.nome}', end=' ')
    print(f'{melancia.nome} e {maracuja.nome}', end=' ')
    print(f'é: {calorias_total_fruta}')