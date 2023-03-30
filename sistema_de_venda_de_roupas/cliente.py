from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, senha: str ):
        super().__init__(nome, cpf)
        self.senha = senha
    
    def get_senha(self):
        return self.senha
    