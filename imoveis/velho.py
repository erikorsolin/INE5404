from imovel import Imovel

class Velho(Imovel):
    def __init__(self) -> None:
        super().__init__()
        p = self.get_preco()
        self.__novo_preco = p - 15/100*p

    def get_novo_preco(self):
        return self.__novo_preco
    
    def imprimir_novo_preco(self):
        print(self.get_novo_preco())