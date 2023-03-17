from normal import Normal
from camarote import CamaroteInferior
from camarote1 import CamaroteSuperior

tipo_ingresso = int(input('Digite 1 para ingresso normal ou 2 para ingresso VIP: '))
if tipo_ingresso == 1:
    ings = Normal()
    ings.imprime_valor()
    ings.imprimir()

elif tipo_ingresso == 2:
    tipo_vip = int(input('Digite 1 para camarote superior ou 2 para camarote inferior: '))
    if tipo_vip == 1:
        ings = CamaroteSuperior()
        ings.imprime_valor()
    elif tipo_vip == 2:
        ings = CamaroteInferior()
        ings.imprime_valor()
        ings.imprimir_localizacao()