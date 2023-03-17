from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float):
        super().__init__(nome, idade, salario)
        self.__cargo = 'Gerente'

    def get_cargo(self):
        return self.__cargo
    
    def exibir_dados(self):
        super().exibir_dados()
        print(self.get_cargo())
