class Pilha:
    def __init__(self) -> None:
        self.itens = []

    def add(self, item):
        self.itens.append(item)
    
    def pop(self):
        self.itens.pop()

    def vazia(self):
        return self.itens == []
    
    def tamanho(self):
        return len(self.itens)
    
    def pegar_item(self):
        return self.itens[-1]


p = Pilha()

p.add('livro 1')
p.add('Livro 2')
p.add('livro 3')

print(p.vazia())
print(p.tamanho())
print(p.pegar_item())
    