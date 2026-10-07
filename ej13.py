class Habitacion:
    def __init__(self, numero, tipo, tarifa_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_noche = tarifa_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print("La habitación ya está ocupada.")
        else:
            self.ocupada = True

    def liberar(self):
        self.ocupada = False

    def calcular_estadia(self, noches):
        if noches <= 0:
            print("La cantidad de noches debe ser positiva.")
            return None
        return self.tarifa_noche * noches

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return (f"Habitación {self.numero} | {self.tipo} | "
                f"{self.tarifa_noche} Gs. por noche | {estado}")


if __name__ == "__main__":
    print("EJERCICIO 13 - Habitación de hotel")
    habitacion = Habitacion(101, "Doble", 250000)
    print(habitacion)
    print("Ocupar habitación")
    habitacion.ocupar()
    print(habitacion)
    print(f"Estadía de 3 noches: {habitacion.calcular_estadia(3)} Gs.")
    print("Intentar ocupar nuevamente")
    habitacion.ocupar()
    print("Intentar calcular una estadía de 0 noches")
    habitacion.calcular_estadia(0)
    print("Liberar habitación")
    habitacion.liberar()
    print(habitacion)
