class Funcionario:
    def __init__(self, nome, idade, salario):
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario
    

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_salario(self):
        return self.__salario

    def exibir_dados(self):
        print(self.get_nome(), self.get_idade(), self.get_salario(), end=' ')

    def set_salario(self, valor):
        self.__salario = valor