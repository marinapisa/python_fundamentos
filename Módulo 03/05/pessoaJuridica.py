from conta import Conta

class PessoaJuridica(Conta):
    __Segundo_Titular = ''
    def __init__(self, titular, cnpj, saldo):
        super().__init__(1409, 'Pessoa Jurídica')
        self.__Titular      = titular
        self.__Cnpj         = cnpj
        self.__Saldo        = saldo

    @property
    def Segundo_Titular(self):
        return self.__Segundo_Titular
    @Segundo_Titular.setter
    def Segundo_Titular(self, segundo_titular):
        self.__Segundo_Titular = segundo_titular
        
    @property
    def titular(self):
        return self.__Titular
    @titular.setter
    def titular(self, titular):
        self.__Titular = titular

    @property
    def cnpj(self):
        return self.__Cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__Cnpj = cnpj

    @property
    def saldo(self):
        return self.__Saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__Saldo = saldo

    def __str__(self):
        return f'{super().__str__()}TITULAR: {self.titular}\nCNPJ: {self.cnpj}\nSALDO: {self.saldo}\nSEGUNDO TITULAR: {self.Segundo_Titular}'