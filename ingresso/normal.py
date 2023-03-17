from ingresso import Ingresso

class Normal(Ingresso):
    def __init__(self) -> None:
        super().__init__()
    def imprimir(self):
        print('Ingresso Normal')