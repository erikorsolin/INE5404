from novo import Novo
from velho import Velho

tipo_imovel = int(input('Digite 1 para imóvel novo ou 2 para imóvel velho: '))
if tipo_imovel == 1:
    imv = Novo()
    print(imv.get_endereco())
    imv.imprimir_novo_preco()
elif tipo_imovel == 2:
    imv = Velho()
    print(imv.get_endereco())
    imv.imprimir_novo_preco()
