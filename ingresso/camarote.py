from vip import Vip

class CamaroteInferior(Vip):
    def __init__(self) -> None:
        super().__init__()
        self.__localizacao = 'plataforma B'

    def get_localizacao(self):
        return self.__localizacao
    
    def imprimir_localizacao(self):
        print(self.__localizacao)