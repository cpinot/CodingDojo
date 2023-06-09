class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cuenta = 0
    def hacer_deposito(self, cantidad):
        self.cantidad = cantidad
        self.cuenta += cantidad
        return self
    def hacer_retiro(self, cantidad):
        self.cantidad = cantidad
        self.cuenta -= cantidad
        return self
    def mostrar_balance(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo: {self.cuenta}")
        return self
    def transferencia(self, usuario, cantidad):
        self.cantidad = cantidad
        self.cuenta -= cantidad
        usuario.cuenta += cantidad
        return self
    
usuario1 = Usuario("Jonatan", "Pereira", 25)
usuario2 = Usuario("Mariana", "Garate", 30) 
usuario3 = Usuario("Andrés", "Meneses", 40)

usuario1.hacer_deposito(200).hacer_deposito(500).hacer_deposito(300).hacer_retiro(150).mostrar_balance()
usuario2.hacer_deposito(900).hacer_deposito(600).hacer_retiro(250).hacer_retiro(150).mostrar_balance()
usuario3.hacer_deposito(1000).hacer_retiro(200).hacer_retiro(300).hacer_retiro(400).mostrar_balance()

usuario1.transferencia(usuario3, 300).mostrar_balance()
usuario3.mostrar_balance()

