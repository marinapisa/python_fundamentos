# 2 - Classe Pessoa: Crie uma classe chamada Pessoa com o atributo nome (public). 
# Implemente métodos set_nome(novo_nome) e get_nome() para manipular esse atributo.


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
         
    def get_nome(self):
        return self.nome

    def set_nome(self, nome_novo):
        print(f'Mudou nome {self.nome} para {nome_novo}')
        self.nome = nome_novo

        # self só usa nos objetos que vem do construtor __ini__
        
if __name__ =='__main__':

    pessoa1 = Pessoa('Marina')
    pessoa2 = Pessoa('Elaine')
    pessoa3 = Pessoa('Maicon')
    
    print(pessoa1.get_nome())
    print(pessoa2.get_nome())
    print(pessoa3.get_nome())

    pessoa1.set_nome('Mauricio')
    pessoa2.set_nome('Mauricio')
    pessoa3.set_nome('Mauricio')

    print(pessoa1.get_nome())
    print(pessoa2.get_nome())
    print(pessoa3.get_nome())