class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} | Precio: {self.precio} Gs."


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return (f"{self.producto.nombre} x {self.cantidad} = "
                f"{self.calcular_subtotal()} Gs.")


class Carrito:
    def __init__(self):
        self._items = []

    def agregar_item(self, item):
        self._items.append(item)

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self._items)

    def mostrar_detalle(self):
        for item in self._items:
            print(item)
        print(self)

    def __str__(self):
        return f"TOTAL: {self.calcular_total()} Gs."


if __name__ == "__main__":
    print("EJERCICIO 10 - Carrito de compras")
    mouse = Producto("Mouse", 150000)
    teclado = Producto("Teclado", 250000)
    auricular = Producto("Auricular", 100000)
    carrito = Carrito()
    carrito.agregar_item(Item(mouse, 2))
    carrito.agregar_item(Item(teclado, 1))
    carrito.agregar_item(Item(auricular, 1))
    carrito.mostrar_detalle()
