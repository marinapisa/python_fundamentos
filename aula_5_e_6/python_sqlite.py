import sqlite3
import os

# criar a classe que irá manipular o banco
    # criar a conexão com o banco

class BancoDeDados:
    # atributo publico da classe
    conexao = None

    @staticmethod #permite acessar este metodo sem criar um objeto
    def criar_conexao( nome_base):
        BancoDeDados.conexao = sqlite3.connect(nome_base)
        print('Conexão estabelecida com sucesso!')
        return BancoDeDados.conexao

    @staticmethod
    def criar_tabela(nome_tabela_nova):
        cursor = BancoDeDados.conexao.cursor()

        sql_string = f'''  
            create table if not exists {nome_tabela_nova} (\
                id integer primary key,\
                nome text(40),\
                numero text(15),\
                email text(40)
            )
        '''

        cursor.execute(sql_string)
        cursor.close()
        print(f'Tabela {nome_tabela_nova} criada com sucesso!')

    @staticmethod
    def insere_dados(nome_tabela, nome_usuario, numero_usuario, email_usuario):
        cursor = BancoDeDados.conexao.cursor()

        sql_string = f"""
            insert into {nome_tabela}\
            (nome, numero, email)\
            values ('{nome_usuario}', '{numero_usuario}', '{email_usuario}')
        """

        cursor.execute(sql_string)
        BancoDeDados.conexao.commit()
        cursor.close()
        print(f'Dados: {nome_usuario} - {numero_usuario} - {email_usuario} inseridos em {nome_tabela} com sucesso')

    @staticmethod
    def deleta_linha(id_linha):
        pass

    @staticmethod
    def mostra_tabela(nome_tabela):
        pass

   

    @staticmethod
    def atualiza_linha(id_linha, nome_novo, numero_novo, email_novo):
        pass



# criar uma funcao main, que sera a interface do usuário

def database_manager():
    os.system('cls')
    conn = BancoDeDados.criar_conexao('base_de_dados.db')
    

    menu_interface = """
1 - Criar Tabela
2 - Inserir dados
3 - Deletar linha
4 - Mostrar tabela
5 - Atualizar linha
6 - Sair
Insira a operação (1 ao 6): """
    while True:
        try:
            operacao = int(input(menu_interface))
            if operacao == 1:
                nome_tabela = input('Informe o nome da nova tabela: ')
                BancoDeDados.criar_tabela(nome_tabela)
            elif operacao == 2:
                tabela = input('Informe o nome da tabela: ')
                nome = input('Informe o nome do contato: ')
                numero= input('Informe o numero do contato: ')
                email= input('Informe o email do contato: ')             
                BancoDeDados.insere_dados(nome_tabela=tabela, nome_usuario=nome, numero_usuario=numero, email_usuario=email)
            elif operacao == 3:
                pass
            elif operacao == 4:
                pass
            elif operacao == 5:
                pass
            elif operacao == 6:
                pass
            else:
                print('Informe uma opção válida!')

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    conn.close()

if __name__ == '__main__':
    database_manager()
    