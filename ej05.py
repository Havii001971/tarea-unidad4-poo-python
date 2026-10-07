class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        precio = f"{self.precio:,.0f}".replace(",", ".")
        return f"{self.marca} {self.modelo} {self.anio} - {precio} Gs."

    def __str__(self):
        return self.descripcion_comercial()


if __name__ == "__main__":
    print("EJERCICIO 5 - Vehículo de una agencia")
    print(Vehiculo("Toyota", "Corolla", 2020, 95000000))
    print(Vehiculo("Kia", "Picanto", 2022, 75000000))
