class Pessoa:
    nome = 'Marina'
    idade = 28
    origem = 'Brasil'

    def dizer_ola(self):
        print(f'Olá eu sou {Pessoa.nome}!')

    def pensar(selt):
        print(f'Eu estou pensando...')

    def comprar(self):
        print(f'Compra realizada!')

    # getter para buscar nome
    def get_nome(self):
        return Pessoa.nome
    
    # getter para buscar idade
    def get_idade(self):
        return Pessoa.idade
    
    # setters para setar o nome
    def set_nome(self, nome_novo):
        Pessoa.nome = nome_novo

    # setters para setar a idade
    def set_idade(self, idade_nova):
        Pessoa.idade = idade_nova
        
# instanciando objetos
pessoa_1 = Pessoa()
pessoa_2 = Pessoa()

# chamando metodos da classe Pessoa via objetos
pessoa_1.comprar()
pessoa_2.pensar()

# chamando os getters
print(pessoa_1.get_nome())
print(pessoa_1.get_idade())

# utilizando os setters
pessoa_1.set_nome('Nayara')
print(pessoa_1.get_nome())
pessoa_2.set_idade(19)
print(pessoa_2.get_idade())


