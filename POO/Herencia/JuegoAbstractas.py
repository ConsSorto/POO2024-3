from abc import ABC, abstractmethod
class Juego:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personajes = []

    def __str__(self):
        print(f"Este es el juego : {self.nombre}")
        for personaje in self.personajes:
            print(personaje)
        return ""
    @staticmethod
    def descripcion():
        return "Esta es la clase de los juegos"
class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.poderes = None
        self.armaduras = []
        self.armas = []

    def __str__(self):
        print(f"Nombre : {self.nombre}")
        for poder in self.poderes:
            print(poder)
        for arma in self.armas:
            print(arma)
        for armadura in self.armaduras:
            print(armadura)
        return ""

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass
class Poder:
    def __init__(self, nombre, descripcion, danno):
        self.nombre = nombre
        self.descripcion = descripcion
        self.danno = danno

    def __str__(self):
        return f"Poder : Nombre : {self.nombre}, descripcion : {self.descripcion}, daño: {self.danno}"
class Armadura:
    def __init__(self, nombre, valorDefensa):
        self.nombre = nombre
        self.valorDefensa = valorDefensa

    def __str__(self):
        return f"Armadura : Nombre : {self.nombre}, valor Defensa : {self.valorDefensa}"
class Arma:
    def __init__(self, nombre, valorDanno):
        self.nombre = nombre
        self.valorDanno = valorDanno

    def __str__(self):
        return f"Arma : Nombre : {self.nombre}, valor Daño : {self.valorDanno}"


class Heroe(Personaje):
    def __init__(self, nombre, objetivo, nivel):
        super().__init__(nombre)
        self.objetivo = objetivo
        self.nivel = nivel
        self.puntosVida = 100

    def atacar(self):
        return "esto es un ataque"
    def defender(self):
        return "esto es una defensa"
class Villano(Personaje):
    def __init__(self, nombre, nivel):
        super().__init__(nombre)
        self.nivel = nivel
        self.puntosVida = 100

class NPC(Personaje):
    def __init__(self, nombre, informacion, servicio):
        super().__init__(nombre)
        self.informacion = informacion
        self.servicio = servicio


heroe = Heroe('Heroe', 'Bueno', 5)