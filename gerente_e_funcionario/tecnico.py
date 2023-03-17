from assistente import Assistente

class Tecnico(Assistente):
    def __init__(self, nome, idade, salario, matricula):
        super().__init__(nome, idade, salario, matricula, tipo='Tecnico')
        self.set_salario(salario + salario*0.2)
    
    def exibir_dados(self):
        super().exibir_dados()
        print(self.get_cargo(), self.get_matricula(), self.get_tipo())