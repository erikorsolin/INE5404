from sistema_vendas import SistemaVendas
from produto import Produto
from cliente import Cliente

loja = SistemaVendas()


logado = False
while True:
    while logado == False:
        decisao = int(input('Digite 1 se já possui possui uma conta ou 2 se deseja fazer o cadastro: '))
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
    print('2 - Ver produtos disponíveis')
    print('3 - Adicionar produto ao carrinho')
    print('4 - Remover prproduto do carrinho')
    print('5 - Consultar preço de um produto')
    print('6 - Ver carrinho')
    print('7 - Consultar preço total do carrinho')
    print('8 - Finalizar compra')
    print('9 - Deslogar')
    print('10 - fechar programa')
    print("="*25)

    acao = int(input('Digite a ação a ser tomada; '))

