from sistema_vendas import SistemaVendas
from produto import Produto
from cliente import Cliente
from carrinho import Carrinho

loja = SistemaVendas()
# Adicionando produtos 
produtos = [Produto(100, 'Camiseta', 'Vermelha', 'G', 50.00),
            Produto(101,'Camiseta', 'Azul', 'G', 50.00),
            Produto(102,'Camiseta', 'Rosa', 'M', 50.00),
            Produto(103,'Camiseta', 'Preto', 'P', 40.00),
            Produto(104, 'Calça', 'Jeans', 'M', 80.90),
            Produto(105,'Calça', 'Azul', 'G', 60.00),
            Produto(106, 'Calça', 'Skynni', 'G', 150.00),
            Produto(107,'Calça', 'Preto', 'G', 100.00),
            Produto(108,'Calça', 'Rosa', 'P', 35.00),
            Produto(109,'Vestido', 'Vermelho', 'M', 135.00),
            Produto(110,'Vestido', 'Rosa', 'P', 100.00),
            Produto(111,'Saia', 'Preto', 'P', 65.00)]
for produto in produtos:
    loja.adicionar_produto(produto)


logado = False
rodando = True

while rodando:
    while not logado:
        decisao = int(input("\n1 - Logar em uma conta existente\n2 - Cadastrar uma conta\nDigite aqui: "))
        print()
        # USUÁRIO JÁ POSSUI CONTA
        if decisao == 1:
            cpf = input('Digite seu cpf: ')
            senha = input('Digite sua senha: ')
            cliente = loja.autenticar_cliente(cpf, senha)
            if cliente == None:
                print('\nCliente não encontrado')
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
    print('-'*35)      
    print('Opções do cliente')
    print('1 - Ver produtos')
    print('2 - Adicionar produto ao carrinho')
    print('3 - Remover produto do carrinho')
    print('4 - Consultar preço de um produto')
    print('5 - Ver produtos no carrinho')
    print('6 - Ver quantidade de produtos no carrinho')
    print('7 - Consultar preço total do carrinho')
    print('8 - Excluir conta')
    print("-"*35)
    print('Opções do administrador')
    print('9 - Adicionar produto ao estoque')
    print('10 - Remover produto do estoque')
    print("-"*35)
    print('Opções gerais')
    print('11 - Deslogar')
    print('12 - Encerrar programa')
    print('-'*35)
    acao = int(input('\nDigite a ação a ser tomada: '))
    print()

    if acao == 1:
        print('Produtos disponíveis:')
        print(f"   {'ID':^12}   {'Tipo':^12}   {'Cor':^12}   {'Tamanho':^12}    {'Preço':^12}\n")
        for produto in loja.get_produtos():
            print(f"-> {produto.get_id():^12} | {produto.get_nome():^12} | {produto.get_cor():^12} | {produto.get_tamanho():^12} | {produto.get_preco():^12}")


    elif acao == 2:
        escolhido = int(input('Digite o ID do produto que deseja adicionar no carrinho: '))
        if not(escolhido in [produto.get_id() for produto in loja.get_produtos()]):
            print('Produto não encontrado')
        else:    
            for produto in loja.get_produtos():
                if produto.get_id() == escolhido: 
                    cliente.carrinho.adicionar_produto(produto)  # cliente tem carrinho como atributo, e carrinho tem o método adicionar_produto()


    elif acao == 3:
        escolhido = int(input('Digite o ID do produto que deseja remover do carrinho: '))
        cliente.carrinho.remover_produto(escolhido)


    elif acao == 4:
        escolhido = int(input('Digite o ID do produto que deseja consultar o preço: '))
        if not(escolhido in [produto.get_id() for produto in loja.get_produtos()]):
            print('Produto não encontrado')
        else:
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
        senha = input('Digite sua senha: ')
        if senha == cliente.get_senha():
            loja.remover_cliente(cliente)
            print('Conta excluída')
            logado = False
            continue
        else:
            print('Senha incorreta')
    

    elif acao in [9, 10]:
        # verificando se o usuário tem permissão para realizar essas ações
        if cliente.get_cpf() == "22213456" and cliente.get_senha() == 'adm123':  # matricula e senha fornecidas pela loja      
            if acao == 9:
                nome = input("Nome do produto: ")
                preco = float(input("Preço do produto: R$"))
                cor = input("Cor do produto: ")
                tamanho = input("Tamanho do produto: ")               
                id = int(input("Id do produto: "))
                loja.adicionar_produto(Produto(id, nome, cor, tamanho, preco))
                print('\nProduto adicionado')

            elif acao == 10:
                id = int(input("Insira o id do produto a ser removido: "))
                produto = loja.buscar_produto_por_id(id)
                if produto:
                    loja.remover_produto(produto)
                    print('Produto removido com sucesso')
                else:
                    print("Produto não cadastrado!")
        else:
            print("Esse usuário não tem permissão para executar esta ação")


    elif acao == 11:
        print('Saindo...')
        logado = False
        continue


    elif acao == 12:
        rodando = False