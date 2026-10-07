class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "Pendiente"

    def marcar_atendido(self):
        self.estado = "Atendido"

    def __str__(self):
        return f"{self.hora} | {self.paciente} | {self.estado}"


class Agenda:
    def __init__(self):
        self._turnos = []

    def agregar_turno(self, turno):
        self._turnos.append(turno)

    def listar_pendientes(self):
        for turno in self._turnos:
            if turno.estado == "Pendiente":
                print(turno)

    def __str__(self):
        return f"Agenda del día | Turnos registrados: {len(self._turnos)}"


if __name__ == "__main__":
    print("EJERCICIO 9 - Turnos de un consultorio")
    agenda = Agenda()
    turnos = [Turno("Ana", "08:00"), Turno("Luis", "08:30"),
              Turno("Marta", "09:00"), Turno("Pedro", "09:30")]
    for turno in turnos:
        agenda.agregar_turno(turno)
    turnos[0].marcar_atendido()
    turnos[2].marcar_atendido()
    print(agenda)
    print("Turnos pendientes:")
    agenda.listar_pendientes()
