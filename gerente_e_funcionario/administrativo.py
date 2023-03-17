from assistente import Assistente

class Administrativo(Assistente):
    def __init__(self, nome: str, idade: int, salario: float, matricula: int, turno: str):
        super().__init__(nome, idade, salario, matricula, tipo='Administrativo')
        self.__turno = turno.upper()
        if self.__turno == 'NOTURNO':
            self.set_salario(salario + salario*0.2)

    def get_turno(self):
        return self.__turno
    
    def exibir_dados(self):
        super().exibir_dados()
        print(self.get_cargo(), self.get_matricula(), self.get_turno(), self.get_tipo())