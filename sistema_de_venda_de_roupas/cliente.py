from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, senha: str, carrinho: object ):
        super().__init__(nome, cpf)
        self.senha = senha
        self.carrinho = carrinho
    
    def get_senha(self):
        return self.senha
    