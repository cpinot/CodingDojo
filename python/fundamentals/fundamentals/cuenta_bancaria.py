
class CuentaBancaria:
    cuentas_corrientes=[]
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interes=0, balance=0): 
        self.banco = "First National Dojo"
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas_corrientes.append(self)

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
            print(f"Banco:{cuenta.banco},Balance: {cuenta.balance}, Tasa de interes: {cuenta.tasa_interes}")
    

cuenta_uno = CuentaBancaria(0.01,500)
cuenta_dos = CuentaBancaria(0.01,800)
cuenta_uno.deposito(100).deposito(200).deposito(300).retiro(50).generar_interes().mostrar_info_cuenta()
cuenta_dos.deposito(100).deposito(200).retiro(50).retiro(50).retiro(50).retiro(50).generar_interes().mostrar_info_cuenta()
cuenta_tres = CuentaBancaria(0.01,1000)
cuenta_tres.deposito(100).deposito(200).retiro(500).retiro(500).retiro(250).retiro(50).generar_interes().mostrar_info_cuenta()
CuentaBancaria.imprimir_cuentas_corrientes()
