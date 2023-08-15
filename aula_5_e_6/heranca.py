# parent class (classe pai/mae)
class Animal:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor
        
    def correr(self):
        print(f'{self.nome} esta correndo....')

    def comer(self):
        print (f'{self.nome} está se alimentando....')

# subclasse herdando classe animal
class Cachorro(Animal):
    def latir(self):
        print('au au i am a dog ......')


class Gato(Animal):
    def destruir_sofa(self):
        print('Seu sofá foi destruido!')


    def miar(self):
        print(' miau miau ....')


cao1 = Cachorro('toddy', 'vermelho')
cao1.comer()
cao1.correr()
cao1.latir()

gato1 = Gato('maria', 'mesclado')
gato1.comer()
gato1.correr()
gato1.destruir_sofa()
gato1.miar()