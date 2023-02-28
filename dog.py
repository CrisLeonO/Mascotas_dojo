from mascotas import Mascota, TiposAnimales


class Perro(Mascota):
    def __init__(self, name, golosinas, salud, energia):
        super().__init__(name, TiposAnimales.PERRO, golosinas, salud, energia)

    def sonido(self):
        print("Guau")
