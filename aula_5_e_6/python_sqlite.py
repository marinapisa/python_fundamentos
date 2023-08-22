import sqlite3
import os

# @staticmethod
# permite aceesar metodo sem criar objetos

class BancoDeDados:
    # Atributo PUBLICO da classe
    conexao = None

    @staticmethod  
    def criar_conexao(nome_base):
        BancoDeDados.conexao = sqlite3.connect(nome_base)
        print('Conexão estabelecida com sucesso.')
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
        print(f'Tabela {nome_tabela_nova} criada com sucesso.')

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
        print(f'Dados: {nome_usuario} - {numero_usuario} - {email_usuario}', end=' ')
        print(f'inseridos em {nome_tabela} com sucesso.')

    @staticmethod
    def delete_linha(id_linha, nome_tabela):
        cursor = BancoDeDados.conexao.cursor()

        sql_query = f'''
            select * from {nome_tabela}
            where id = {id_linha}
        '''
        cursor.execute(sql_query)
        dados_banco = cursor.fetchall() #retorna tudo

        if len(dados_banco) > 0:
            sql_delete = f'''
            delete from {nome_tabela}
            where id = {id_linha}
        '''
        
            cursor.execute(sql_delete)
            cursor.close()
            BancoDeDados.conexao.commit()
            print(f'Linha {id_linha} deletada com sucesso!')
        else:
            print(f'Tabela {nome_tabela} com id {id_linha} não existe.')


    @staticmethod
    def mostra_tabela(nome_tabela):
        cursor = BancoDeDados.conexao.cursor()
        sql_query = f'''
            select * from {nome_tabela}
        '''

        cursor.execute(sql_query)

        dados_banco = cursor.fetchall()
        if len(dados_banco) > 0 :
            print(f'\nDados da tabela {nome_tabela}:\n')
            for linha in dados_banco:
                for coluna in linha:
                    print(coluna, end=' ')
                print('\n')
                
            cursor.close()
        else:
            print(f'A tabela {nome_tabela} não possui registros!')


    @staticmethod
    def atualiza_linha(id_linha, nome_tabela, nome_novo, numero_novo, email_novo):
        cursor = BancoDeDados.conexao.cursor()

        sql_query = f'''
            select * from {nome_tabela}
            where id = {id_linha}
        '''
        cursor.execute(sql_query)
        dados_banco = cursor.fetchall() #retorna tudo

        if len(dados_banco) > 0:
            sql_update = f"""
            update {nome_tabela}
            set nome = '{nome_novo}', 
            numero = '{numero_novo}', 
            email = '{email_novo}'
            where id = {id_linha}
        """
        
            cursor.execute(sql_update)
            cursor.close()
            BancoDeDados.conexao.commit()
            print(f'Linha {id_linha} atualizada com sucesso!')
        else:
            print(f'Tabela {nome_tabela} com id {id_linha} não existe.')

    @staticmethod
    def valida_colunas_banco(nome, numero, email):
        # VALIDA NOME = PRECISA TER NO MINIMO 3 CARACTERES E NAO PODE TER NUMERO
        valida_nome = True
        numeros = ['1', '2', '3', '4', '5', '6', '7','8', '9', '0']
        if len(nome) >= 3:

            nome = list(nome) #transforma o nome em lista
            for letra in nome: 
                if letra in numeros:
                    valida_nome = False
            # se letras maior q 3  e cada letra do estiver na lista de numeros então valida_nome é falso

        else:
            print('O nome precisa ter 3 ou mais caracteres e nao pode ter numeros.')
            valida_nome = False
            #  se ele nao entrar nesse if vai ser false
        
        
        # VALIDA EMAIL = PRECISA TER @ e . e PELO MENOS 10 CARACTERES
        valida_email = False
        if len(email)>=10 and '@'in email and '.' in email:
            valida_email = True
        else:
            print('O e-mail precisa ter os simbolos @ e . e pelo menos 10 caracteres')
        

        # VALIDA NUMERO = SÓ PODE TER NUMERO E/OU SIMBOLOS: +, (), -
        # precisa ter pelo menos 8 numeros
        #  o len nao pode ser maior que 14
        lista_simbolos = ['+', '(', ')', '-']
        lista_numeros = ['1', '2', '3', '4', '5', '6', '7','8', '9', '0']
        valida_numero = False
        if len(numero) >= 8 and len(numero) <= 14:

            numero_lista = list(numero)
            contador = 0
            for number in numero_lista:
                if number in lista_numeros or number in lista_simbolos:
                    if number in lista_numeros:
                        contador += 1
                    elif number not in numeros and number not in lista_simbolos:
                        contador = 0
                        break

            if contador >= 8:
                    valida_numero = True
                
        else:
            print('O numero precisa ter entre 8 e 14 digitos')
        

        return valida_email and valida_nome and valida_numero

        # return precisa ser um boolean para verificar se validou os dados ou não

def database_manager():
    os.system('cls')
    conn = BancoDeDados.criar_conexao('base_de_dados.db')

    menu_interface = '''
1 - Criar tabela
2 - Inserir dados
3 - Deletar linha
4 - Mostrar tabela
5 - Aualizar linha
6 - Sair
Insira a operação (1 - 6): '''

    while True:
        try:
            operacao = int(
                input(menu_interface)
            )

            if operacao == 1:
                nome_tabela = input('Informe o nome da tabela nova: ')
                BancoDeDados.criar_tabela(nome_tabela)

            elif operacao == 2:
                tabela = input('Informe o nome da tabela: ')
                nome = input('Informe o nome do contato: ')
                numero = input('Informe o número do contato: ')
                email = input('Informe o e-mail do contato: ')

                dados_validos = BancoDeDados.valida_colunas_banco(nome = nome, numero = numero, email = email)
            
                if dados_validos is True:

                    BancoDeDados.insere_dados(
                        nome_tabela=tabela,
                        nome_usuario=nome,
                        numero_usuario=numero,
                        email_usuario=email
                    )

            elif operacao == 3:
                tabela = input('Informe o nome da tabela: ')
                id_linha = input('Informe o ID da linha: ')
                BancoDeDados.delete_linha(id_linha = id_linha, nome_tabela = tabela)

            elif operacao == 4:
                tabela = input('Informe o nome da tabela: ')
                BancoDeDados.mostra_tabela(nome_tabela=tabela)

            elif operacao == 5:
                tabela = input('Informe o nome da tabela: ')
                id_linha = input('Informe o id da linha a alterar: ')
                nome = input('Informe o novo nome do contato: ')
                numero = input('Informe o novo número do contato: ')
                email = input('Informe o novo e-mail do contato: ')

                dados_validos = BancoDeDados.valida_colunas_banco(nome = nome, numero = numero, email = email)

                if dados_validos is True:

                    BancoDeDados.atualiza_linha(
                        id_linha = id_linha,
                        nome_tabela = tabela,
                        nome_novo = nome,
                        numero_novo = numero,
                        email_novo = email
                    )
                    
            elif operacao == 6:
                print('Programa encerrado.')
                break
            else:
                print(
                    'Informe uma operação válida'
                )

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    conn.close()
    print('Conexão encerrada.')
            

if __name__ == '__main__':
    database_manager()
    # print(BancoDeDados.valida_colunas_banco(nome = 'Marina', numero = '123444554', email = 'marina@marina.com'))
    