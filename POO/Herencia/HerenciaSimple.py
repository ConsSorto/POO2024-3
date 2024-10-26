# Figuras Geometricas, Area y Perimetro
# Cuadrado
# Rectangulo
# Circulo

import math

class Figura:
    def __init__(self, tipo):
        self.tipo = tipo

    def imprimirTipo(self):
        print(self.tipo)
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        super().__init__('Cuadrado')

    def calcularArea(self):
        return self.lado*self.lado

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        super().__init__('Rectangulo')

    def calcularArea(self):
        return self.lado1*self.lado2


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        super().__init__('Circulo')

    def calcularArea(self):
        return math.pi * self.radio * self.radio

cuadrado = Cuadrado(5)

cuadrado.imprimirTipo()
print(cuadrado.calcularArea())

rectangulo = Rectangulo(2,5)

rectangulo.imprimirTipo()
print(rectangulo.calcularArea())

circulo = Circulo(5)
circulo.imprimirTipo()
print(circulo.calcularArea())


