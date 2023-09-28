class Casa:
    def __init__(self, cor, tamanho, comodos, banheiros):
        self.__Cor          : str = cor
        self.__Tamanho      : int = tamanho
        self.__Comodos      : int = comodos
        self.__Banheiros    : int = banheiros

    @property
    def cor(self):
        return self.__Cor
    @cor.setter
    def cor(self, cor):
        self.__Cor = cor

    @property
    def tamanho(self):
        return self.__Tamanho
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__Tamanho = tamanho

    @property
    def comodos(self):
        return self.__Comodos
    @comodos.setter
    def comodos(self, comodos):
        self.__Comodos = comodos

    @property
    def banheiros(self):
        return self.__Banheiros
    @banheiros.setter
    def banheiros(self, banheiros):
        self.__Banheiros = banheiros

    def __str__(self):
        return f'\ncor: {self.cor}\ntamanho: {self.tamanho}\ncomodos: {self.comodos}\nbanheiros: {self.banheiros}'
