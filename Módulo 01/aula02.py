nome: str = 'Andre'
sobrenome: str = 'Granemann'
idade: int = 25

# concatenação
print('Nome', nome, 'sobrenome', sobrenome, 'idade', idade)

# interpolação
print(f'Nome {nome} sobrenome {sobrenome} idade {idade}')

# mascara de substituição
print('nome {}sobrenome {} idade {}'.format(nome, sobrenome, idade))

#  os 3 paradigmas do python são: estruturado (papiro), funcional(livro) e orientado a objeto(caça-palavras)