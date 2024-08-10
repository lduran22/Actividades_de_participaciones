class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios  
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Depósito de ${monto:.2f} realizado con éxito.")
        else:
            print("El monto de depósito debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.balance:
                self.balance -= monto
                print(f"Retiro de ${monto:.2f} realizado con éxito.")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("El monto de retiro debe ser positivo.")

    def aplicar_cuota_manejo(self):
        porcentaje = 0.02 
        cuota = self.balance * porcentaje
        self.balance -= cuota
        print(f"Cuota de manejo de ${cuota:.2f} aplicada. Balance actualizado.")

    def __str__(self):
        return (f"Número de cuenta: {self.numero_cuenta}\n"
                f"Propietarios: {', '.join(self.propietarios)}\n"
                f"Balance: ${self.balance:.2f}")


propietarios = ["Juan Pérez", "Ana Gómez"]
cuenta = CuentaBancaria("1234567890", propietarios, 1000.00)

print(cuenta)  

cuenta.depositar(500.00)  
print(cuenta)  

cuenta.aplicar_cuota_manejo()  
print(cuenta)  
