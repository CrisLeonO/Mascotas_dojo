from mascotas import Mascota, TiposAnimales


class Gato(Mascota):
    def __init__(self, name, golosinas, salud, energia):
        super().__init__(name, TiposAnimales.GATO, golosinas, salud, energia)

    def sonido(self):
        print("Miau")
