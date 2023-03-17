from funcionario import Funcionario

class Assistente(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, matricula: int, tipo: str):
        super().__init__(nome, idade, salario)
        self.__matricula = matricula
        self.__cargo = 'Assistente'
        self.__tipo = tipo
    
    def get_matricula(self):
        return self.__matricula

    def get_cargo(self):
        return self.__cargo
    
    def get_tipo(self):
        return self.__tipo