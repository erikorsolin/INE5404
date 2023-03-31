from sistema_vendas import SistemaVendas
from produto import Produto
from cliente import Cliente
from carrinho import Carrinho

loja = SistemaVendas()
# Adicionando produtos 
produtos = [Produto(1234, 'Camiseta', 'Vermelha', 'G', 50.00),
            Produto(1263,'Camiseta', 'Azul', 'G', 50.00),
            Produto(6587,'Camiseta', 'Rosa', 'M', 50.00),
            Produto(9000,'Camiseta', 'Preto', 'P', 40.00),
            Produto(1324, 'Calça', 'Jeans', 'M', 80.90),
            Produto(8909,'Calça', 'Azul', 'G', 60.00),
            Produto(1237, 'Calça', 'Skynni', 'G', 150.00),
            Produto(9866,'Calça', 'Preto', 'G', 100.00),
            Produto(4356,'Calça', 'Rosa', 'P', 35.00)]
for produto in produtos:
    loja.adicionar_produto(produto)


logado = False
while True:
    while logado == False:
        decisao = int(input('Digite 1 se já possui possui uma conta ou 2 se deseja fazer o cadastro: '))

        # USUÁRIO JÁ POSSUI CONTA
        if decisao == 1:
            cpf = input('Digite seu cpf: ')
            senha = input('Digite sua senha: ')
            cliente = loja.autenticar_cliente(cpf, senha)
            if cliente == None:
                print('Cliente não encontrado')
            else:
                print()
                print(f'É bom te ver novamente {cliente.get_nome()} :), você está logado!')
                logado = True
        
        # USUÁRIO NÃO POSSUI CONTA
        elif decisao == 2:
            nome = input('Digite seu nome: ')
            cpf = input('Digite seu cpf: ')
            senha = input('Digite sua senha: ')
            cliente = Cliente(nome, cpf, senha)
            loja.adicionar_cliente(cliente)
            print()
            print(f'Bem vindo(a) {cliente.get_nome()}, você está logado!')
            logado = True
            
            
    print("="*25)
    print('Opções do cliente')
    print('1 - Ver produtos')
    print('2 - Adicionar produto ao carrinho')
    print('3 - Remover prproduto do carrinho')
    print('4 - Consultar preço de um produto')
    print('5 - Ver carrinho')
    print('6 - Consultar preço total do carrinho')
    print('7 - Finalizar compra')
    print('8 - Deslogar')
    print('9 - fechar programa')
    print("="*25)
    acao = int(input('Digite a ação a ser tomada: '))

    if acao == 1:
        for produto in loja.get_produtos():
            print(f"{produto.get_id():^10} | {produto.get_nome():^10} | {produto.get_cor():^10} | {produto.get_tamanho():^10} | {produto.get_preco():^10}")


    elif acao == 2:
        escolhido = int(input('Digite o ID do produto que deseja adicionar no carrinho: '))
        for produto in loja.get_produtos():
            if produto.get_id() == escolhido:
                cliente.carrinho.adicionar_produto(produto) # cliente tem carrinho como atributo, e carrinho tem o método adicionar_produto()

    elif acao == 3:
        escolhido = int(input('Digite o ID do produto que deseja remover do carrinho: '))
        cliente.carrinho.remover_produto(produto)

    elif acao == 4:
        escolhido = int(input('Digite o ID do produto que deseja consultar o preço: '))
        for produto in loja.get_produtos():
            if produto.get_id == escolhido:
                print(f'o preço do produto é {produto.get_preco()} R$')

    





