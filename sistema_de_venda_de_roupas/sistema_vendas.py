from carrinho import Carrinho
class SistemaVendas:
    def __init__(self):
        self.produtos = []
        self.clientes = []

    def get_produtos(self):
        return self.produtos
    
    def get_clientes(self):
        return self.clientes
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def buscar_produto_por_id(self, id):
        for produto in self.produtos:
            if produto.get_id() == id:
                return produto
        return None

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def autenticar_cliente(self, cpf, senha):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf and cliente.get_senha() == senha:
                return cliente
        return None