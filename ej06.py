class CuentaCorriente:
    def __init__(self, cliente, saldo=0):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.cliente = cliente
        self.saldo = saldo

    def acreditar(self, monto):
        if monto <= 0:
            print("El monto debe ser positivo.")
            return
        self.saldo += monto

    def consumir(self, monto):
        if monto <= 0:
            print("El monto debe ser positivo.")
        elif monto > self.saldo:
            print("Saldo insuficiente. Compra rechazada.")
        else:
            self.saldo -= monto

    def __str__(self):
        return f"Cliente: {self.cliente} | Saldo: {self.saldo} Gs."


if __name__ == "__main__":
    print("EJERCICIO 6 - Cuenta corriente")
    cuenta = CuentaCorriente("Ana López", 50000)
    print(f"Estado inicial: {cuenta}")
    print("Acreditar 100000 Gs.")
    cuenta.acreditar(100000)
    print(cuenta)
    for monto in [40000, 60000, 80000]:
        print(f"Comprar por {monto} Gs.")
        cuenta.consumir(monto)
        print(cuenta)
    print("Intentar acreditar 0 Gs.")
    cuenta.acreditar(0)
    print(cuenta)
