class Conta:
    def __init__(self, numero, tipo):
        self.Numero     = numero
        self.Tipo       = tipo

    def __str__(self):
        return f'NUMERO DA AGENCIA: {self.Numero}\nTIPO DA CONTA: {self.Tipo}\n'