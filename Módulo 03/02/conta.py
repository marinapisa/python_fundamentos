class Conta:
    # inicio de uma classe- entrada
    def __init__(self, numero, titular, cpf, saldo, limite):
        
        self.Numero     : int = numero
        self.Titular    : str = titular
        self.Cpf        : str = cpf
        self.Saldo      : str = saldo
        self.Limite     : str = limite

        
   # final de uma classe - saída
    def __str__(self):
        return f'{self.Numero} {self.Titular} {self.Cpf} {self.Saldo} {self.Limite}'