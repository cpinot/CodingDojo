class Mascota:
    def __init__(self, nombre, tipo, golosinas):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 0
        self.energia = 0

    def comer(self):
        self.energia += 5
        self.salud += 10
        print(f"Salud aumenta a {self.salud} y energia aumenta a {self.energia}")
        return self

    def dormir(self):
        self.energia += 25
        print(f"Energia aumenta a {self.energia}")
        return self
    
    def jugar(self):
        self.salud += 5
        print(f"Salud aumenta a {self.salud}")
        return self
    
    def ruido(self):
        print("Guau!")
        return self
    
    #hacer una subclase de mascota que sea perro y que tenga un metodo que se llame ruido y que haga guau
    #hacer una subclase de mascota que sea gato y que tenga un metodo que se llame ruido y que haga miau

class Perro(Mascota):
    def __init__(self, nombre, tipo, golosinas):
        super().__init__(nombre, tipo, golosinas)
    
    def ruido(self):
        print("Guau!")
        return self

class Gato(Mascota):
    def __init__(self, nombre, tipo, golosinas):
        super().__init__(nombre, tipo, golosinas)
    
    def ruido(self):
        print("Miau!")
        return self