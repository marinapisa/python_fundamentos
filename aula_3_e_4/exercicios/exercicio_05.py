# 5 - Classe Triângulo:
# Crie uma classe chamada Triangulo que represente um triângulo. A classe deve ter os atributos lado1, 
# lado2 e lado3.
# Crie métodos para verificar se os lados formam um triângulo válido (eh_valido()), calcular o perímetro 
# (calcular_perimetro())
# e exibir o tipo do triângulo com base nos lados (tipo_triangulo()).

class Triangulo:
    def __init__(self, lado_1, lado_2, lado_3):
        self._lado_1 = lado_1
        self._lado_2 = lado_2
        self._lado_3 = lado_3
        print('Objeto instanciado com sucesso!')

    def eh_valido(self):
        lado_1_valido = self._lado_3 + self._lado_2 > self._lado_1
        lado_2_valido = self._lado_1 + self._lado_3 > self._lado_2
        lado_3_valido = self._lado_1 + self._lado_2 > self._lado_3

        return lado_1_valido is True and lado_2_valido is True and lado_3_valido is True

    def calcula_perimetro(self):
        return self._lado_1 + self._lado_2 + self._lado_3
    
    def tipo_triangulo(self):
        if self._lado_1 == self._lado_2 and self._lado_1 == self._lado_3:
            print('Este triângulo é Equilátero')
        elif self._lado_1 != self._lado_2 and self._lado_1 != self._lado_3 and self._lado_2 != self._lado_3:
            print('Este triângulo é Escaleno')
        else:
            print('Este triângulo é Isósceles')

    

triangulo_1 = Triangulo(4, 6, 7)
triangulo_2 = Triangulo(2, 3, 5)
triangulo_3 = Triangulo(2, 2, 2)
triangulo_4 = Triangulo(2, 3, 2)

if __name__ == '__main__':
    print(f'Triangulo 1 é válido: {triangulo_1.eh_valido()}')
    print(f'Triangulo 2 é válido: {triangulo_2.eh_valido()}')

    print(f'Triangulo 1 perimetro: {triangulo_1.calcula_perimetro()}')
    print(f'Triangulo 2 perimetro: {triangulo_2.calcula_perimetro()}')

    triangulo_1.tipo_triangulo()
    triangulo_2.tipo_triangulo()
    triangulo_3.tipo_triangulo()
    triangulo_4.tipo_triangulo()

