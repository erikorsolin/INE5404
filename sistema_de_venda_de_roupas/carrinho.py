class Carrinho:
    def __init__(self) -> None:
        self.produtos = list()
        self.preco_total = 0
        self.quantidade_produtos = 0

    def get_produtos(self):
        return self.produtos
    
    def get_preco_total(self):
        return self.preco_total
    
    def get_quantidade_produtos(self):
        return self.quantidade_produtos
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.preco_total += produto.get_preco()
        self.quantidade_produtos += 1
        print(f"produto  ({produto.get_nome()} | {produto.get_cor()} | {produto.get_tamanho()})  adicionado com sucesso")
    
    def remover_produto(self, id):
        for produto in self.produtos:
            if produto.get_id() == id:
                self.produtos.remove(produto)
                self.quantidade_produtos -= 1
                self.preco_total -= produto.get_preco()
                print(f"produto  ({produto.get_nome()} | {produto.get_cor()} | {produto.get_tamanho()})  removido com sucesso")
                return
        print('Produto não está no carrinho')


   
