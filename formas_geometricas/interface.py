from circulo import Circulo
from quadrado import Quadrado
from quadrilateros import Quadrilateros
from retangulo import Retangulo

def calcular_circulo(raio):
    c1 = Circulo(raio)
    perimetro = c1.raio*2*3.14
    area = (c1.raio**2)*3.14
    print('O perímetro do circulo é {}\nA área do circulo é: {}'.format(perimetro, area))

def calcular_quadrado(lado):
    q1 = Quadrado(lado)
    perimetro = 4*lado
    area = lado**2
    print('O perímetro do quadrado é: {}\nA área do quadrado é: {}'.format(perimetro, area))

def calcular_quadrilatero(lado1, lado2, lado3, lado4):
    k = Quadrilateros(lado1, lado2, lado3, lado4)
    perimetro = k.calculo_perimetro()
    print('O perímetro do quadrilatero é: {}'.format(perimetro))

def calcular_retangulo(base, altura):
    r1 = Retangulo(base, altura)
    perimetro = 2*r1.base + 2*r1.altura
    area = r1.base * r1.altura
    print('O perímetro do retangulo é: {}\nA área do retangulo é: {}'.format(perimetro, area))



qtd_formas = int(input('Digite quantas formas deseja calcular: '))
for forma in range(qtd_formas):
    print('digite 1 para Quadrado\ndigite 2 para circulo\ndigite 3 para retangulo\ndigite 4 para retangulo\n')
    tipo = int(input())
    if tipo == 1:
        lado = int(input('digite o lado: '))
        calcular_quadrado(lado)
    elif tipo == 2:
        raio = int(input('digite o raio: '))
        calcular_circulo(raio)
    elif tipo == 3:
        base, altura = [int(x) for x in(input('Digite a base e a altura: ').split())]
        calcular_retangulo(base, altura)
    elif tipo == 4:
        lado1, lado2, lado3, lado4 = [int(x) for x in (input('Digite os lados do quadrilatero: ').split())]
        calcular_quadrilatero(lado1, lado2, lado3, lado4)
    print()



