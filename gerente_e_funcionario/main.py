from administrativo import Administrativo
from tecnico import Tecnico
from assistente import Assistente

p1 = Administrativo('erik', 19, 2000, 22102195, 'noturno')
p1.exibir_dados()

print('---------------')
print('---------------')

p2 = Tecnico('LUIGI', 23, 3000, 2334)
p2.exibir_dados()

print('---------------')
print('---------------')

p3 = Administrativo('larissa', 19, 2000, 22102195, 'diurno')
p3.exibir_dados()