class LineaTelefonica:
    def __init__(self, cliente, gigas_incluidos):
        if gigas_incluidos <= 0:
            raise ValueError("El plan debe incluir una cantidad positiva de gigas.")
        self.cliente = cliente
        self.gigas_incluidos = gigas_incluidos
        self.gigas_consumidos = 0

    def registrar_consumo(self, gigas):
        if gigas <= 0:
            print("El consumo debe ser positivo.")
        elif gigas > self.gigas_disponibles():
            print("El paquete de datos se agotó.")
        else:
            self.gigas_consumidos += gigas
            if self.gigas_disponibles() == 0:
                print("El paquete de datos se agotó.")

    def gigas_disponibles(self):
        return self.gigas_incluidos - self.gigas_consumidos

    def __str__(self):
        return (f"{self.cliente} | Plan: {self.gigas_incluidos} GB | "
                f"Consumo: {self.gigas_consumidos} GB | "
                f"Disponibles: {self.gigas_disponibles()} GB")


if __name__ == "__main__":
    print("EJERCICIO 12 - Plan de datos")
    linea = LineaTelefonica("Ana López", 10)
    print(linea)
    for gigas in [3, 4, 3, 2, 0]:
        print(f"Intentar consumir {gigas} GB")
        linea.registrar_consumo(gigas)
        print(linea)
