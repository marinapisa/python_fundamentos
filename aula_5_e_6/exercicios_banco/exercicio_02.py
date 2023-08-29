# 2 - Neste exercício, você criará uma hierarquia de classes envolvendo uma classe abstrata Pessoa, com subclasses Aluno e Professor.
# Cada classe deve implementar métodos específicos, usando conceitos de abstração, herança e programação orientada a objetos (POO).
# Crie uma classe abstrata chamada Pessoa com o método abstrato exibir_info() e calcular_salario().
# Implemente o método exibir_info() para exibir informações básicas da pessoa, como nome e idade.
# Implemente o método calcular_salario() como um método abstrato, que será diferente para cada subclasse.
# Crie uma subclasse Aluno que herde da classe Pessoa.
# Implemente o método exibir_info() para exibir informações específicas de um aluno, como nome, idade e número de matrícula.
# Implemente o método calcular_salario() para alunos, que, neste caso, não se aplica. Pode ser um método vazio.
# Crie uma subclasse Professor que herde da classe Pessoa.
# Implemente o método exibir_info() para exibir informações específicas de um professor, como nome, idade e disciplina lecionada.
# Implemente o método calcular_salario() para professores, calculando o salário com base na carga horária e valor por hora.
# Crie instâncias de Aluno e Professor.
# Chame o método exibir_info() para cada instância para verificar a exibição correta das informações.
# Chame o método calcular_salario() para o professor e exiba o valor calculado.
# Utilize a biblioteca sqlite3 para criar uma tabela chamada Pessoas com os campos tipo (para distinguir entre aluno e professor),
# nome, idade, info_extra (número de matrícula para aluno, disciplina para professor) e salario (nullable para aluno).
# Implemente métodos para adicionar instâncias de Aluno e Professor à tabela Pessoas, extraindo as informações dos métodos exibir_info()
# e calcular_salario() e outros métodos que trabalhem comandos SQL atráves de métodos / funções em Python.

import sqlite3
import os
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade,):
        self.nome = nome
        self.idade = idade
       
    @abstractmethod
    def exibir_info():
        pass

    
    @abstractmethod
    def calcular_salario():
        pass



class Aluno(Pessoa):
    def exibir_info(self):
        print('Dados do Aluno: ')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')


    def calcular_salario(self):
        print('Método Calcular salário não se aplica a alunos.')

          
class Professor(Pessoa):
    def __init__(self,disciplina, salario, carga_horaria):
        self.disciplina = disciplina
        self.salario = salario
        self.carga_horaria = carga_horaria

    def exibir_info(self):
        print('Dados do professor: ')
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Disciplina: {self.disciplina}')
      
    
    
    def calcular_salario(self):
        # Implemente o método calcular_salario() para professores, calculando o salário com base na carga horária e valor por hora.










    def calcular_idade
        

        self.idade
    

        




joao = Pessoa('joao', 19)
bruno = Pessoa('bruno', 56)

joao.calcular_idade()
