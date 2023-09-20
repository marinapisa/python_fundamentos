from controller import create, read, search, update, delete


def menu():
    cond = 'sim'
    while cond == 'sim':
        var = int(input('1 - Criar\n2 - Listar\n3 - Pesquisar\n4 - Alterar\n5 - Deletar\n>>'))
        match(var):
            case 1:
                pessoa = {}
                pessoa['Nome']      = input('Digite seu nome:')
                pessoa['cpf']       = input('Digite seu cpf:')
                pessoa['idade']     = int(input('Digite sua idade:'))
                pessoa['telefone']  = input('Digite seu telefone:')
                create(pessoa)
            case 2:
                print(read())
            case 3:
                pass
            case 4:
                update(input('Digite o nome da pessoa que deseja alterar: '))
            case 5:
                delete(input('Informe o cliente que deseja deletar: '))
        cond = input('Deseja continuar\nSim\nNão')

menu()




# create(input('digite seu nome: '))
# print(read())
# search(input('Digite o nome que deseja pesquisar:'))
# update(input('Digite a pessoa que deseja atualizar: '))

