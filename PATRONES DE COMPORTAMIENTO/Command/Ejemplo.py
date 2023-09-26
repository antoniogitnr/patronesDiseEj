from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """
    La interfaz Command declara un método para ejecutar un comando.
    """
    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):
    """
    Algunos comandos pueden implementar operaciones simples por sí mismos.
    """
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Mira, puedo hacer cosas simples como imprimir"
              f"({self._payload})")

class ComplexCommand(Command):
    """
    Sin embargo, algunos comandos pueden delegar operaciones más complejas a otros
    objetos, llamados "receptores".
    """
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Los comandos complejos pueden aceptar uno o varios objetos receptores junto con
        cualquier dato de contexto a través del constructor.
        """
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Los comandos pueden delegar a cualquier método de un receptor.
        """
        print("ComplexCommand: Las tareas complejas deberían ser realizadas por un objeto receptor", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    """
    Las clases Receptoras contienen lógica empresarial importante. Saben cómo
    realizar todo tipo de operaciones asociadas con la ejecución de una solicitud. De
    hecho, cualquier clase puede actuar como un Receptor.
    """
    def do_something(self, a: str) -> None:
        print(f"\nReceptor: Trabajando en ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceptor: También trabajando en ({b}.)", end="")

class Invoker:
    """
    El Invocador está asociado con uno o varios comandos. Envía una solicitud
    al comando.
    """
    _on_start = None
    _on_finish = None

    """
    Inicializa los comandos.
    """
    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        El Invocador no depende de clases de comando o receptor concretas. El
        Invocador pasa una solicitud a un receptor de forma indirecta, ejecutando un
        comando.
        """
        print("Invocador: ¿Alguien quiere algo antes de que comience?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invocador: ...haciendo algo realmente importante...")

        print("Invocador: ¿Alguien quiere algo después de que termine?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

if __name__ == "__main__":
    """
    El código del cliente puede parametrizar un invocador con cualquier comando.
    """
    invocador = Invoker()
    invocador.set_on_start(SimpleCommand("¡Di Hola!"))
    receptor = Receiver()
    invocador.set_on_finish(ComplexCommand(
        receptor, "Enviar correo electrónico", "Guardar informe"))
    invocador.do_something_important()