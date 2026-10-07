class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} | Autor: {self.autor} | {estado}"


if __name__ == "__main__":
    print("EJERCICIO 4 - Libro de una biblioteca")
    print(Libro("El principito", "Antoine de Saint-Exupéry"))
    print(Libro("Yo el Supremo", "Augusto Roa Bastos", False))
