from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

class Originator():
    """
    El Originator mantiene un estado importante que puede cambiar con el tiempo.
    También define un método para guardar el estado en un memento y otro método
    para restaurar el estado desde él.
    """
    _state = None
    """
    Por simplicidad, el estado del originator se almacena en una variable única.
    """
    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: Mi estado inicial es: {self._state}")

    def do_something(self) -> None:
        """
        La lógica del negocio del Originator puede afectar su estado interno.
        Por lo tanto, el cliente debe hacer una copia de seguridad del estado antes de
        ejecutar los métodos de la lógica del negocio a través del método save().
        """
        print("Originator: Estoy haciendo algo importante.")
        self._state = self._generate_random_string(30)
        print(f"Originator: y mi estado ha cambiado a: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        Guarda el estado actual en un memento.
        """
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Restaura el estado del Originator a partir de un objeto memento.
        """
        self._state = memento.get_state()
        print(f"Originator: Mi estado ha cambiado a: {self._state}")

class Memento(ABC):
    """
    La interfaz Memento proporciona una forma de recuperar los metadatos del memento,
    como la fecha de creación o el nombre. Sin embargo, no expone el estado del Originator.
    """
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        El Originator utiliza este método al restaurar su estado.
        """
        return self._state

    def get_name(self) -> str:
        """
        El resto de los métodos se utilizan para mostrar metadatos por el Caretaker.
        """
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date

class Caretaker():
    """
    El Caretaker no depende de la clase ConcreteMemento. Por lo tanto, no tiene acceso al
    estado del Originator almacenado dentro del memento. Trabaja con todos los mementos a través
    de la interfaz Memento base.
    """
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Guardando el estado del Originator...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        print(f"Caretaker: Restaurando estado a: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Aquí está la lista de mementos:")
        for memento in self._mementos:
            print(memento.get_name())

if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nCliente: ¡Ahora, vamos a deshacer!\n")
    caretaker.undo()

    print("\nCliente: ¡Una vez más!\n")
    caretaker.undo()