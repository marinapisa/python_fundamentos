from dojo_casa import Casa

casa1 = Casa('Azul', 120, 5, 2)

casa_Rodrigo = Casa(
                input('Digite a cor da casa do Rodrigo: '),
                int(input('Digite os mt2 da sua casa: ')),
                int(input('Digite a qtd de comodos: ')),
                int(input('Digite a qtd de banheiros: '))
                )
casa_Marina = Casa(
                input('Digite a cor da casa da Marina: '),
                int(input('Digite os mt2 da sua casa: ')),
                int(input('Digite a qtd de comodos: ')),
                int(input('Digite a qtd de banheiros: '))
                )
casa_Carlos = Casa(
                input('Digite a cor da casa do Carlos: '),
                int(input('Digite os mt2 da sua casa: ')),
                int(input('Digite a qtd de comodos: ')),
                int(input('Digite a qtd de banheiros: '))
                )
casa_Adrian = Casa(
                input('Digite a cor da casa do Adrian: '),
                int(input('Digite os mt2 da sua casa: ')),
                int(input('Digite a qtd de comodos: ')),
                int(input('Digite a qtd de banheiros: '))
                )

# casa_Marina.cor = casa_Rodrigo.cor
# casa_Carlos.cor = casa_Adrian.cor

print('Rodrigo >> ', casa_Rodrigo)
print('='*30)
print('Marina >>', casa_Marina)
print('='*30)
print('Carlos >>', casa_Carlos)
print('='*30)
print('Adrian >>', casa_Adrian)
print('='*30)