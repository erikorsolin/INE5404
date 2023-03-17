from ingresso import Ingresso

class Vip(Ingresso):
    def __init__(self) -> None:
        super().__init__()
        self.set_preco_ingresso(150)