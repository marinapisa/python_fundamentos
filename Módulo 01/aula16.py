cond = 'sim'

# lower() transforma td em minuscula
# upper() transforma em maiuscula
# capitalize() transforma a primeira em maiuscula

while cond.capitalize() == 'Sim':
    var = input('Digite seu nome para testarmos a interação >>')
    print(f'O nome digitado pelo usuário foi {var}')

    cond = input('Você deseja continuar?\nsim\nnao\n>>')

print('Você saiu do sistema!')