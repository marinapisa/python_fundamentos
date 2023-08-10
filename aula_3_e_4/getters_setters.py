class Animal:
  
    # Construtor

    # private -> __nome
    # protected -> _nome 
    # public -> nome


    def __init__(self, raca, cor, idade, nome):
        self._raca = raca
        self._cor = cor
        self._idade = idade
        self.__nome = nome
        print('Objeto instanciado com sucesso!')


    # GETTERS

    @property
    def raca(self):
        return 'Raça -> ' + self._raca

    @property
    def cor(self):
        return 'Cor -> ' + self._cor
    
    @property
    def idade(self):
        return f'Idade ->  {self._idade}'
    
    @property
    def nome(self):
        return f'Nome ->  {self.__nome}'
    
    # SETTERS

    @raca.setter
    def raca(self, raca_nova):
        print(f'setou raça {self._raca} para {raca_nova}')
        self._raca = raca_nova

    @cor.setter
    def cor(self, cor_nova):
        print(f'setou cor {self._cor} para {cor_nova}')
        self._cor = cor_nova
    
    @idade.setter
    def idade(self, idade_nova):
        print(f'setou idade {self._idade} para {idade_nova}')
        self._idade = idade_nova
    
    @nome.setter
    def nome(self, nome_novo):
        print(f'setou nome {self.__nome} para {nome_novo}')
        self.__nome = nome_novo

# Instancias (criações) dos objetos da classe animal
leao = Animal('leao da montanha', 'bege', 15, 'valente')
gato = Animal('persa', 'cinza', 2, 'mimi')
pantera = Animal('pantera cor de rosa', 'rosa', 11, 'bruce')

# utilizar getters para cada objeto
print(leao.raca)
print(leao.cor)
print(leao.idade)

print(gato.raca)
print(gato.cor)
print(gato.idade)

print(pantera.raca)
print(pantera.cor)
print(pantera.idade)

# UTILIZAR SETTERS
pantera.idade = 56
print(pantera.idade)
pantera.cor = 'verde'
print(pantera.cor)
gato.raca = 'siames'
print(gato.raca)

print(pantera.nome)




























# # while True:
#     try:
#         metodo = input('Informe o método ou S para sair: ')
#         if metodo.lower() == 'get_raca':
#             print(Animal.get_raca())    

#         elif metodo.lower() == 'get_cor':
#             print(Animal.get_cor())

#         elif metodo.lower() == 'get_idade':
#             print(Animal.get_idade())

#         elif metodo.lower() == 'set_raca':
#             raca = input('Informe a raça: ')
#             Animal.set_raca(raca)

#         elif metodo.lower() == 'set_cor':
#             cor = input('Informe a cor: ')
#             Animal.set_cor(cor)

#         elif metodo.lower() == 'set_idade':
#             idade = input('Informe a idade: ')
#             Animal.set_idade(idade)  

#         elif metodo.lower() == 's':
#             print('Programa encerrado!!')
#             break      

#     except Exception as erro:
#         print(f'Ocorreu um erro: {erro}')