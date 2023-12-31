# 1 - Classe Produto:
# Crie uma classe chamada Produto que represente um produto em uma loja. A classe deve ter os atributos: nome (private), preco
# e codigo (public). Crie um construtor para inicializar esses atributos e métodos get_nome(), get_preco() e set_preco(novo_preco) para
# acessar e modificar o preço.



class Produto:
    def __init__(self, nome, preco, codigo):
        self.__nome = nome
        self.preco = preco
        self.codigo = codigo
        print('objeto instanciado!')

    # Getters:
    @property #para poder acessar itena privados
    def nome (self):
        return 'Nome: ' + self.__nome
    
    def get_preco (self):
        return f'Preço:  + {self.preco}'
    
    def get_codigo (self):
        return f'Código:  + {self.codigo}'
    
    # Setters:
    @nome.setter #por ser privado
    def nome(self, nome_novo):
        print(f'setou nome {self.__nome} para {nome_novo}')
        self.__nome = nome_novo
        #print precisa vir antes do atributo receber o novo valor para a frase ficar correta
        

    def set_preco(self, preco_novo):
        print(f'setou preço {self.preco} para {preco_novo}')
        self.preco = preco_novo
        

    def set_codigo(self, codigo_novo):
        print(f'setou codigo {self.codigo} para {codigo_novo}')
        self.codigo = codigo_novo

if __name__ == '__main__':

    # criando os objetos de cada produto
    produto_01 = Produto('Café', 15, 1001)
    produto_02 = Produto('Chocolate', 7, 1002)
    produto_03 = Produto('Amendoas', 10, 1003)


    # acessando os dados ja cadastrados dos itens (getter):
    print(produto_01.nome)
    print(produto_01.get_preco())
    print(produto_01.get_codigo())

    print(produto_02.nome)
    print(produto_02.get_preco())
    print(produto_02.get_codigo())

    print(produto_03.nome)
    print(produto_03.get_preco())
    print(produto_03.get_codigo())

    # modificando os dados dos itens (setter):
    produto_01.nome = 'Meia'
    produto_01.set_preco(6)
    produto_01.set_codigo(2001)

    print(produto_01.nome)
    print(produto_01.get_preco())
    print(produto_01.get_codigo())