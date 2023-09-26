from abc import ABC, abstractmethod

# Interfaz Mediator
class Mediator(ABC):
    @abstractmethod
    def enviar_mensaje(self, mensaje: str, colleague: 'Colleague') -> None:
        pass

# Implementación del Mediator
class ConcreteMediator(Mediator):
    def __init__(self):
        self.colleagues = []

    def agregar_colleague(self, colleague: 'Colleague') -> None:
        self.colleagues.append(colleague)

    def enviar_mensaje(self, mensaje: str, colleague: 'Colleague') -> None:
        for c in self.colleagues:
            if c != colleague:
                c.recibir_mensaje(mensaje)

# Interfaz Colleague
class Colleague(ABC):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass

    @abstractmethod
    def recibir_mensaje(self, mensaje: str) -> None:
        pass

# Implementación del Colleague
class ConcreteColleague(Colleague):
    def enviar(self, mensaje: str) -> None:
        print(f"Enviando mensaje: {mensaje}")
        self.mediator.enviar_mensaje(mensaje, self)

    def recibir_mensaje(self, mensaje: str) -> None:
        print(f"Recibiendo mensaje: {mensaje}")

# Ejemplo de uso
if __name__ == "__main__":
    mediator = ConcreteMediator()

    colleague1 = ConcreteColleague(mediator)
    colleague2 = ConcreteColleague(mediator)
    colleague3 = ConcreteColleague(mediator)

    mediator.agregar_colleague(colleague1)
    mediator.agregar_colleague(colleague2)
    mediator.agregar_colleague(colleague3)

    colleague1.enviar("¡Hola a todos!")