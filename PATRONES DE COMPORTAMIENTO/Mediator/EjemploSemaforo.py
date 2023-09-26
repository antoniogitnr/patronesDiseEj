from abc import ABC, abstractmethod

# Interfaz Mediator
class Mediator(ABC):
    @abstractmethod
    def notificar_cambio(self, semaforo: 'Semaforo') -> None:
        pass

# Implementación del Mediator
class InterseccionMediator(Mediator):
    def __init__(self):
        self.semaforos = []

    def agregar_semaforo(self, semaforo: 'Semaforo') -> None:
        self.semaforos.append(semaforo)

    def notificar_cambio(self, semaforo: 'Semaforo') -> None:
        for s in self.semaforos:
            if s != semaforo:
                s.cambiar_estado()

# Interfaz Colleague
class Semaforo(ABC):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    @abstractmethod
    def cambiar_estado(self) -> None:
        pass

# Implementación del Colleague
class SemaforoPeatonal(Semaforo):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)
        self.estado = "Verde"

    def cambiar_estado(self) -> None:
        if self.estado == "Verde":
            self.estado = "Rojo"
        else:
            self.estado = "Verde"
        print(f"Semaforo peatonal cambió a estado: {self.estado}")

# Implementación del Colleague
class SemaforoVehicular(Semaforo):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)
        self.estado = "Rojo"

    def cambiar_estado(self) -> None:
        if self.estado == "Rojo":
            self.estado = "Verde"
        else:
            self.estado = "Rojo"
        print(f"Semaforo vehicular cambió a estado: {self.estado}")

# Ejemplo de uso
if __name__ == "__main__":
    mediator = InterseccionMediator()

    semaforo_peatonal = SemaforoPeatonal(mediator)
    semaforo_vehicular = SemaforoVehicular(mediator)

    mediator.agregar_semaforo(semaforo_peatonal)
    mediator.agregar_semaforo(semaforo_vehicular)

    semaforo_peatonal.cambiar_estado()
    semaforo_vehicular.cambiar_estado()