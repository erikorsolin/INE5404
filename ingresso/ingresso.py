class Ingresso:
    def __init__(self) -> None:
        self.__preco_ingresso = 100
        
    def imprime_valor(self):
        print(self.__preco_ingresso)
    
    def set_preco_ingresso(self, v):
        self.__preco_ingresso = v