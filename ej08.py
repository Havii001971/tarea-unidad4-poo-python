class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} - {self.artista} | {self.duracion} min"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self._canciones = []  # Colección interna, administrada por los métodos.

    def agregar_cancion(self, cancion):
        self._canciones.append(cancion)

    def calcular_duracion_total(self):
        return sum(cancion.duracion for cancion in self._canciones)

    def mostrar_lista(self):
        print(self)
        for cancion in self._canciones:
            print(cancion)
        print(f"Duración total: {self.calcular_duracion_total():.1f} min")

    def __str__(self):
        return f"Lista: {self.nombre} | Canciones: {len(self._canciones)}"


if __name__ == "__main__":
    print("EJERCICIO 8 - Lista de reproducción")
    lista = ListaReproduccion("Para estudiar")
    lista.agregar_cancion(Cancion("Amanecer", "Dúo Sur", 3.5))
    lista.agregar_cancion(Cancion("El camino", "Luna", 4))
    lista.agregar_cancion(Cancion("Atardecer", "Dúo Sur", 2.5))
    lista.mostrar_lista()
