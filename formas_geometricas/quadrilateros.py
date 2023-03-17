class Quadrilateros:
    def __init__(self, lado1, lado2, lado3, lado4) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4

    def calculo_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3 + self.lado4
    
    
