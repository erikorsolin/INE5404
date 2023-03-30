class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco
    
    def get_nome(self):
        return self.nome
    
    def get_preco(self):
        return self.preco
