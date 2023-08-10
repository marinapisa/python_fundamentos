class Animal:
  
    # Construtor
    def __init__(self, raca, cor, idade):
        self.raca = raca
        self.cor = cor
        self.idade = idade
        print('Objeto instanciado com sucesso!')


    # GETTERS

    @property
    def raca(self):
        return 'Raça -> ' + self.raca

    @property
    def cor(self):
        return 'Cor -> ' + self.cor
    
    @property
    def idade(self):
        return f'Idade ->  {self.idade}'
    
    # SETTERS

    def set_raca(self, raca_nova):
        self.raca = raca_nova

    def set_cor(self, cor_nova):
        self.cor = cor_nova
    
    def set_idade(self, idade_nova):
        self.idade = idade_nova

# Instancias (criações) dos objetos da classe animal
leao = Animal('leao da montanha', 'bege', 15)
gato = Animal('persa', 'cinza', 2)
pantera = Animal('pantera cor de rosa', 'rosa', 11)

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