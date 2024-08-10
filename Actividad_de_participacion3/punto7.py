class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios 
        self.balance = balance

    def __str__(self):
        return (f"Número de cuenta: {self.numero_cuenta}\n"
                f"Propietarios: {', '.join(self.propietarios)}\n"
                f"Balance: ${self.balance:.2f}")


propietarios = ["Juan Pérez", "Ana Gómez"]
cuenta = CuentaBancaria("1234567890", propietarios, 1000.00)

print(cuenta)
