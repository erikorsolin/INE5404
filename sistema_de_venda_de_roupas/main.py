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
            Produto(4356,'Calça', 'Rosa', 'P', 35.00),
            Produto(4358,'Vestido', 'Vermelho', 'M', 135.00),
            Produto(4359,'Vestido', 'Rosa', 'P', 100.00),
            Produto(4360,'Saia', 'Preto', 'P', 65.00)]
for produto in produtos:
    loja.adicionar_produto(produto)


logado = False
rodando = True

while rodando:
    while not logado:
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
            
    print()        
    print("="*25)
    print('Opções do cliente')
    print('1 - Ver produtos')
    print('2 - Adicionar produto ao carrinho')
    print('3 - Remover produto do carrinho')
    print('4 - Consultar preço de um produto')
    print('5 - Ver produtos no carrinho')
    print('6 - Ver quantidade de produtos no carrinho')
    print('7 - Consultar preço total do carrinho')
    print('8 - Excluir conta')
    print('9 - Deslogar')
    print('10 - Fechar programa')
    print("="*25)
    acao = int(input('Digite a ação a ser tomada: '))
    print()

    if acao == 1:
        print('Produtos disponíveis')
        for produto in loja.get_produtos():
            print(f"-> {produto.get_id():^10} | {produto.get_nome():^10} | {produto.get_cor():^10} | {produto.get_tamanho():^10} | {produto.get_preco():^10}")


    elif acao == 2:
        escolhido = int(input('Digite o ID do produto que deseja adicionar no carrinho: '))
        if not(escolhido in [produto.get_id() for produto in loja.get_produtos()]):
            print('Produto não encontrado')
            
        for produto in loja.get_produtos():
            if produto.get_id() == escolhido: 
                cliente.carrinho.adicionar_produto(produto)  # cliente tem carrinho como atributo, e carrinho tem o método adicionar_produto()


    elif acao == 3:
        escolhido = int(input('Digite o ID do produto que deseja remover do carrinho: '))
        cliente.carrinho.remover_produto(escolhido)


    elif acao == 4:
        escolhido = int(input('Digite o ID do produto que deseja consultar o preço: '))
        for produto in loja.get_produtos():
            if produto.get_id() == escolhido:
                print(f'O preço do produto é {produto.get_preco()} R$')

    
    elif acao == 5:
        if cliente.carrinho.get_produtos() == None:
            print('Carrinho vazio')
        else:
            for produto in cliente.carrinho.get_produtos():
                print(f"{produto.get_id():^10} | {produto.get_nome():^10} | {produto.get_cor():^10} | {produto.get_tamanho():^10} | {produto.get_preco():^10}")
    

    elif acao == 6:
        print(f'A quantidade de produtos no carrinho é {cliente.carrinho.get_quantidade_produtos()}')
        


    elif acao == 7:
        print(f'O preço total do carrinho é: {cliente.carrinho.get_preco_total()} R$')
    

    elif acao == 8:
        loja.remover_cliente(cliente)
        print('Conta excluída')
        logado = False
        continue
    

    elif acao == 9:
        print('Saindo...')
        logado = False
        continue
    

    elif acao == 10:
        rodando = False