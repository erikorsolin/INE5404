from carrinho import Carrinho
class SistemaVendas:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.vendas = []

    def get_produtos(self):
        return self.produtos
    
    def get_cliente(self):
        return self.clientes
    
    def get_vendas(self):
        return self.vendas

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def buscar_produto_por_nome(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def autenticar_cliente(self, cpf, senha):
        for cliente in self.clientes:
            if cliente.cpf == cpf and cliente.senha == senha:
                return cliente
        return None

    def registrar_venda(self, cliente):
        venda = Carrinho(cliente)
        self.vendas.append(venda)