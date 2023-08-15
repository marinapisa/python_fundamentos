# 4 - Classe Funcionário:
# Crie uma classe chamada Funcionario com os atributos nome (private), salario (private) e cargo (public). Crie métodos para definir o nome
# (set_nome(novo_nome)), obter o nome (get_nome()), calcular aumento de salário (aumentar_salario(aumento)) e exibir informações completas do
# funcionário (exibir_informacoes()). Crie um construtor e trabalhe a manipulação da classe e dos dados via objetos.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.cargo = cargo
        
    # getter privado
    @property 
    def nome(self):
        return self.__nome
    
    # setter privado 
    @nome.setter
    def nome(self, nome_novo):
        self.__nome = nome_novo

    def aumenta_salario (self, valor_acrescimo):
        self.__salario = self.__salario + valor_acrescimo

    def exibe_informações(self):
        print(f'Funcionário {self.__nome}, possui salário R${self.__salario} e exerce cargo {self.cargo}')
   
        
if __name__ =='__main__':
    funcionario1 = Funcionario('Marina', 6000, 'Analista de Suporte PL')
    funcionario2 = Funcionario('Jennifer', 4000, 'Analista de Suporte JR')

    print(funcionario1.nome)
    funcionario1.exibe_informações()
    print(funcionario2.nome)
    funcionario2.exibe_informações()
    funcionario2.aumenta_salario(1000)
    funcionario2.exibe_informações()
