class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_valor_stock(self):
        return self.precio * self.stock

    def __str__(self):
        return f"{self.nombre} | Precio: {self.precio} Gs. | Stock: {self.stock}"


if __name__ == "__main__":
    print("EJERCICIO 2 - Producto de almacén")
    productos = [Producto("Arroz", 8000, 10), Producto("Leche", 6500, 20)]
    for producto in productos:
        print(producto)
        print(f"Valor del stock: {producto.calcular_valor_stock()} Gs.")
