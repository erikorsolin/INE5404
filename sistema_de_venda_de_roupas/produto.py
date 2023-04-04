class Produto:
    def __init__(self, id: int, nome: str, cor: str, tamanho: str, preco: float) -> None:
        self.id = id
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
    
    def get_id(self):
        return self.id
       
    def get_nome(self):
        return self.nome
    
    def get_cor(self):
        return self.cor
    
    def get_tamanho(self):
        return self.tamanho
    
    def get_preco(self):
        return self.preco
    
    def set_id(self, id):
        self.id = id
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_cor(self, cor):
        self.cor = cor
    
    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    def set_preco(self, preco):
        self.preco = preco