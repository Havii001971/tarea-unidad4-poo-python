class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return (f"Cliente: {self.nombre}\n"
                f"Cédula: {self.cedula}\nTeléfono: {self.telefono}")


if __name__ == "__main__":
    print("EJERCICIO 1 - Ficha de cliente")
    print(Cliente("Ana López", "4567890", "0981 111222"))
    print()
    print(Cliente("Luis Vera", "5678901", "0982 333444"))
