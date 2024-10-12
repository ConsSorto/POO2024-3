class Alumno:
    # Nombre
    # Nota1
    # Nota2
    # Nota3
    # Nota4
    # Promedio
    def __init__(self, Nombre, Nota1, Nota2, Nota3, Nota4):
        self._Nombre = Nombre
        self.Nota1 = Nota1
        self.Nota2 = Nota2
        self.Nota3 = Nota3
        self.Nota4 = Nota4

    def calcularPromedio(self):
        self.Promedio = (self.Nota1 + self.Nota2 + self.Nota3 + self.Nota4) / 4
    def DatosAlumno(self):
        return (self._Nombre, self.Promedio)

    def setNombre(self, nombre):
        self._Nombre = nombre

    def getNombre(self):
        return self._Nombre


