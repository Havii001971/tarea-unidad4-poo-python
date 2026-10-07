class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self):
        return self.salario_mensual * 13  # 12 meses y un aguinaldo.

    def __str__(self):
        return f"{self.nombre} | {self.cargo} | Mensual: {self.salario_mensual} Gs."


if __name__ == "__main__":
    print("EJERCICIO 3 - Empleado y su sueldo")
    empleados = [Empleado("Ana López", "Cajera", 3000000),
                 Empleado("Luis Vera", "Vendedor", 3500000)]
    for empleado in empleados:
        print(empleado)
        print(f"Salario anual (13 salarios): {empleado.calcular_salario_anual()} Gs.")
