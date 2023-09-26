class Subsystem1:
    def operation1(self) -> str:
        return "Operación 1 del Subsistema 1"

    def operation2(self) -> str:
        return "Operación 2 del Subsistema 1"


class Subsystem2:
    def operation1(self) -> str:
        return "Operación 1 del Subsistema 2"

    def operation2(self) -> str:
        return "Operación 2 del Subsistema 2"


class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self) -> str:
        results = []
        results.append("Iniciando operación a través del Facade:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append(self._subsystem1.operation2())
        results.append(self._subsystem2.operation2())
        return "\n".join(results)


def client_code(facade: Facade) -> None:
    print(facade.operation())


if __name__ == "__main__":
    facade = Facade()
    client_code(facade)