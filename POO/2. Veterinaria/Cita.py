class Cita:
    def __init__(self, nombre, peso, dueno):
        self.nombre = nombre
        self.peso =peso
        self.dueno = dueno
        self.estado = "esperando"

    def __str__(self):
        return f"Nombre: {self.nombre}, Peso: {self.peso}, Dueno: {self.dueno}, Estado: {self.estado}"

