class CuentaBancaria:
    cuentas_corrientes=[]
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interes=0, balance=0): 
        self.banco = "First National Dojo"
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.cuenta=CuentaBancaria.cuentas_corrientes.append(self)
        

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        if(self.balance < amount):
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self
    @classmethod
    def imprimir_cuentas_corrientes (cls):
        for cuenta in cls.cuentas_corrientes:
            print(f"Cuenta:{cuenta.banco},Balance: {cuenta.balance}, Tasa de interes: {cuenta.tasa_interes}")
class Usuario:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cuenta=CuentaBancaria()

    def hacer_deposito(self, cantidad):
        self.cuenta.deposito(cantidad)
        return self
    
    def hacer_retiro(self, cantidad):
        self.cuenta.retiro(cantidad)
        return self
    
    def mostrar_balance(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Chequeando banco:{self.cuenta.banco} , Saldo: {self.cuenta.balance}")
        return self
    
    def transferencia(self, usuario, cantidad):
        self.cantidad = cantidad
        self.cuenta -= cantidad
        usuario.cuenta += cantidad




    
usuario1 = Usuario("Jonatan", "Pereira", 25)
usuario2 = Usuario("Mariana", "Garate", 30)
usuario3 = Usuario("Andrés", "Meneses", 40)

usuario1.hacer_deposito(200).hacer_deposito(500).hacer_deposito(300).hacer_retiro(150).mostrar_balance()
usuario2.hacer_deposito(900).hacer_deposito(600).hacer_retiro(250).hacer_retiro(150).mostrar_balance()

