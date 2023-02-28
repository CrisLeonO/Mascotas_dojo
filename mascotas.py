from enum import Enum


class TiposAnimales(Enum):
    PERRO = 1
    GATO = 2
    MICO = 3


class Mascota:
    def __init__(self, name, tipo, golosinas, salud, energia):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia

    def dormir(self):
        print("ZzZzZzZ")
        self.energia += 25

    def comer(self, alimento):
        print("Que rico, vamos a comer: " + alimento)
        self.energia += 5
        self.salud += 10

    def jugar(self):
        print("Jugando")
        self.salud += 5

    def sonido(self):
        print("*Inserte aqui el ruido de la mascota*")


