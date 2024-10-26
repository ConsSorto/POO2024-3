# Figuras Geometricas, Area y Perimetro
# Cuadrado
# Rectangulo

class Figura:
    def __init__(self, tipo):
        self.tipo = tipo


    def imprimirTipo(self):
        print(self.tipo)

    def Mostrar(self):
        print('Funcion Mostrar de figura')
class Rectangulo:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def calcularArea(self):
        return self.lado1 * self.lado2

    def Mostrar(self):
        print('Funcion Mostrar de rectangulo')

class Cuadrado(Figura, Rectangulo):
    def __init__(self, lado):
        Figura.__init__(self, 'Cuadrado')
        Rectangulo.__init__(self, lado, lado)
        self.lado = lado

    def MostrarFigura(self):
        Figura.Mostrar(self)

    def MostrarRectangulo(self):
        Rectangulo.Mostrar(self)


cuadrado = Cuadrado(5)

cuadrado.imprimirTipo()
print(cuadrado.calcularArea())
cuadrado.Mostrar()
cuadrado.MostrarFigura()
cuadrado.MostrarRectangulo()