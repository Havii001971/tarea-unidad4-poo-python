class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def registrar_nota(self, materia, nota):
        if not 0 <= nota <= 100:
            print("La nota debe estar entre 0 y 100.")
            return
        self.notas[materia] = nota

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas.values()) / len(self.notas)

    def esta_aprobado(self):
        return self.calcular_promedio() >= 60

    def mostrar_boletin(self):
        print(self)
        for materia, nota in self.notas.items():
            print(f"{materia}: {nota}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        condicion = "Aprobado" if self.esta_aprobado() else "Reprobado"
        print(f"Condición final: {condicion}")

    def __str__(self):
        return f"Estudiante: {self.nombre}"


if __name__ == "__main__":
    print("EJERCICIO 11 - Estudiante y sus materias")
    estudiante = Estudiante("Ana López")
    estudiante.registrar_nota("Matemática", 80)
    estudiante.registrar_nota("Python", 95)
    estudiante.registrar_nota("Inglés", 65)
    print("Intentar registrar una nota de 120:")
    estudiante.registrar_nota("Historia", 120)
    estudiante.mostrar_boletin()
