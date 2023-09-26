class Conta:
    __Numero = 123
    # construtor
    def __init__(self, titular, cpf, saldo, limite):
        
        self.__Titular    : str = titular
        self.__Cpf        : str = cpf
        self.__Saldo      : str = saldo
        self.__Limite     : str = limite

    # set insere (sempre que é privado) get pega
    def set_numero(self, numero):
        self.__Numero = numero
    def get_numero(self):
        return self.__Numero
    
    def set_titular(self, titular):
        self.__Titular = titular
    def get_titular(self):
        return self.__Titular
    
    def set_cpf(self, cpf):
        self.__Cpf = cpf
    def get_cpf(self):
        return self.__Cpf
    
    def set_saldo(self, saldo):
        self.__Saldo = saldo
    def get_saldo(self):
        return self.__Saldo
    
    def set_limite(self, limite):
        self.__Limite = limite
    def get_limite(self):
        return self.__Limite

        
   # final de uma classe - saída
    def __str__(self):
        return f'{self.get_numero} {self.get_} {self.Cpf} {self.Saldo} {self.Limite}'