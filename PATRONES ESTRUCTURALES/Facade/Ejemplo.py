from __future__ import annotations

class Facade:
    """
    La clase Facade proporciona una interfaz simple para la lógica compleja de uno o
    varios subsistemas. El Facade delega las solicitudes del cliente a los
    objetos apropiados dentro del subsistema. El Facade también es responsable de
    gestionar su ciclo de vida. Todo esto protege al cliente de la complejidad no deseada
    del subsistema.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Dependiendo de las necesidades de su aplicación, puede proporcionar al Facade
        objetos de subsistema existentes o forzar al Facade a crearlos por sí mismo.
        """
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        Los métodos del Facade son atajos convenientes para la funcionalidad sofisticada
        de los subsistemas. Sin embargo, los clientes solo tienen acceso a una fracción
        de las capacidades de un subsistema.
        """
        results = []
        results.append("El Facade inicializa los subsistemas:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("El Facade ordena a los subsistemas realizar la acción:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    El Subsistema puede aceptar solicitudes tanto del facade como del cliente directamente.
    En cualquier caso, para el Subsistema, el Facade es simplemente otro cliente y no forma
    parte del Subsistema.
    """

    def operation1(self) -> str:
        return "Subsistema1: ¡Listo!"

    # ...

    def operation_n(self) -> str:
        return "Subsistema1: ¡Adelante!"


class Subsystem2:
    """
    Algunos facades pueden trabajar con múltiples subsistemas al mismo tiempo.
    """

    def operation1(self) -> str:
        return "Subsistema2: ¡Prepárate!"

    # ...

    def operation_z(self) -> str:
        return "Subsistema2: ¡Fuego!"


def client_code(facade: Facade) -> None:
    """
    El código del cliente trabaja con subsistemas complejos a través de una interfaz simple
    proporcionada por el Facade. Cuando un facade gestiona el ciclo de vida del
    subsistema, el cliente puede que ni siquiera sepa de la existencia del
    subsistema. Este enfoque le permite mantener la complejidad bajo control.
    """
    print(facade.operation(), end="")


if __name__ == "__main__":
    # El código del cliente puede tener algunos objetos del subsistema ya creados.
    # En este caso, puede ser conveniente inicializar el Facade con estos
    # objetos en lugar de permitir que el Facade cree nuevas instancias.
    subsistema1 = Subsystem1()
    subsistema2 = Subsystem2()
    facade = Facade(subsistema1, subsistema2)
    client_code(facade)