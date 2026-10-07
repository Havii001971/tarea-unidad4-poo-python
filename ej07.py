class ProductoStock:
    def __init__(self, nombre, stock, stock_minimo):
        if stock < 0 or stock_minimo < 0:
            raise ValueError("El stock y su mínimo no pueden ser negativos.")
        self.nombre = nombre
        self.stock = stock
        self.stock_minimo = stock_minimo

    def _comprobar_stock(self):
        if self.stock < self.stock_minimo:
            print("ALERTA: es necesario reponer stock.")

    def ingresar_mercaderia(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return
        self.stock += cantidad
        self._comprobar_stock()

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
        elif cantidad > self.stock:
            print("Stock insuficiente. Venta rechazada.")
        else:
            self.stock -= cantidad
            self._comprobar_stock()

    def __str__(self):
        return f"{self.nombre} | Stock: {self.stock} | Mínimo: {self.stock_minimo}"


if __name__ == "__main__":
    print("EJERCICIO 7 - Control de stock con alertas")
    producto = ProductoStock("Arroz", 10, 5)
    print(f"Estado inicial: {producto}")
    print("Ingresar 5 unidades")
    producto.ingresar_mercaderia(5)
    print(producto)
    for cantidad in [6, 5, 10, 0]:
        print(f"Vender {cantidad} unidades")
        producto.vender(cantidad)
        print(producto)
