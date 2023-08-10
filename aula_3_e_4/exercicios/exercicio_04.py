# 4 - Classe Agenda:
# Crie uma classe chamada Agenda que represente uma agenda de contatos. A classe deve ter um atributo para 
# armazenar uma lista de contatos.
# Crie métodos para adicionar (adicionar_contato(nome, telefone)), remover (remover_contato(nome)), e 
# exibir todos os contatos (exibir_contatos()).

class Agenda:
    lista_contatos = []

    def adicionar_contato(novo_item):
        Agenda.lista_contatos.append(novo_item)
        print(f'Item {novo_item} adicionado com sucesso!')

    def remover_contato(posicao):
        Agenda.lista_contatos.pop(posicao)
        print(f'Item na posição {posicao} removido com sucesso!')

    def exibir_info():
        if len(Agenda.lista_contatos) > 0:
            for indice, valor in enumerate(Agenda.lista_contatos):
                print(f'posição: {indice} \n Valor: {valor}')
        else:
            print('A lista esta vazia!')

    def rodar_script():
        while True:
            try:
                metodo = input('Informe o método ou S para sair ')
                if metodo.lower() == 'adicionar':
                    novo_item = input('Informe o novo item: ')
                    Agenda.adicionar_contato(novo_item)
                elif metodo.lower() == 'remover':
                    posicao = int(input('Informe a posição: '))
                    Agenda.remover_contato(posicao)
                elif metodo.lower() == 'exibir':
                    Agenda.exibir_info()
                elif metodo.lower() == 's':
                    print('programa encerrado!!')
                    break

            except Exception as erro:
                print(f'Ocorreu um erro: {erro}')


if __name__ == '__main__':
    Agenda.rodar_script()