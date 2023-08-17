# 4 - Crie uma classe abstrata Animal com um método emitir_som(). Crie subclasses Cachorro,
#     Gato, Cavalo e Vaca que herdam de Animal e implementam seus próprios sons. Crie uma função
#     que aceita uma lista de animais e faça-os emitir sons usando polimorfismo.
#     Em seguida, crie contrutores para as subclasses dando um atributo nome e cor, e crie
#     objetos dessas subclasses com cores e nomes distintos.

from abc import ABC, abstractmethod

# CLASSE ABSTRATA (MODELO)
class Animal(ABC):
     def __init__(self, marca, modelo, ligado):
         self.marca = marca
         self.modelo = modelo
         self.ligado = ligado
        

     @abstractmethod #quando tiver @ é decoradores
     def emitir_sim(self):
        pass

     @abstractmethod
     def desligar(self):
        pass

# SUBCLASSES

class Cachorro




if __name__ == '__main__':