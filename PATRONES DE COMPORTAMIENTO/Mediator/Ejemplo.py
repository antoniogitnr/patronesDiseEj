from __future__ import annotations
from abc import ABC

class Mediator(ABC):
    """
    La interfaz Mediator declara un método utilizado por los componentes para
    notificar al mediador sobre varios eventos. El mediador puede reaccionar a
    estos eventos y pasar la ejecución a otros componentes.
    """
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("El mediador reacciona a A y desencadena las siguientes operaciones:")
            self._component2.do_c()
        elif event == "D":
            print("El mediador reacciona a D y desencadena las siguientes operaciones:")
            self._component1.do_b()
            self._component2.do_c()

class BaseComponent:
    """
    El componente base proporciona la funcionalidad básica de almacenar una
    instancia del mediador dentro de los objetos de componente.
    """
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

"""
Los componentes concretos implementan diversas funcionalidades. No dependen de
otros componentes. Tampoco dependen de ninguna clase mediadora concreta.
"""
class Component1(BaseComponent):
    def do_a(self) -> None:
        print("El Componente 1 hace A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("El Componente 1 hace B.")
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("El Componente 2 hace C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("El Componente 2 hace D.")
        self.mediator.notify(self, "D")

if __name__ == "__main__":
    # Código del cliente.
    c1 = Component1()
    c2 = Component2()
    mediador = ConcreteMediator(c1, c2)

    print("El cliente desencadena la operación A.")
    c1.do_a()
    print("\n", end="")

    print("El cliente desencadena la operación D.")
    c2.do_d()