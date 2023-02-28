class Ninja:
    def __init__(self, nombre, apellido, mascotas, premio, comida_mascotas):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascotas = comida_mascotas

    def caminar(self):
        print("Caminar")
        for mascota in self.mascotas:
            mascota.jugar()

    def alimentar(self):
        print("Alimentando las mascotas")
        for mascota in self.mascotas:
            mascota.comer(
                self.comida_mascotas.get(mascota.tipo, "Pan")
            )

    def bañar(self):
        print("Bañando")
        for mascota in self.mascotas:
            mascota.sonido()
