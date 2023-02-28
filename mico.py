from mascotas import Mascota, TiposAnimales


class Mico(Mascota):
    def __init__(self, name, golosinas, salud, energia):
        super().__init__(name, TiposAnimales.MICO, golosinas, salud, energia)

    def sonido(self):
        print("UUhh UaHH uuuhh")
