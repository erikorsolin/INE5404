class Pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf 

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf
        