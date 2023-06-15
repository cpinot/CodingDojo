
class Ninja:
    def __init__(self, nombre, apellido, mascotas, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        print(f"{self.mascotas.nombre} está caminando")
        self.mascotas.jugar()
        return self
    
    def alimentar(self):
        print(f"{self.mascotas.nombre} se está alimentando")
        self.mascotas.comer()
        return self
    
    def bañar(self):
        print(f"{self.mascotas.nombre} se está bañando")
        self.mascotas.ruido()
        return self
    