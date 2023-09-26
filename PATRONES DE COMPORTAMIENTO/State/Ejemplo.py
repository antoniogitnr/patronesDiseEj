from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
    El Contexto define la interfaz de interés para los clientes. También mantiene
    una referencia a una instancia de una subclase de Estado, que representa el estado actual
    del Contexto.
    """
    _state = None
    """
    Una referencia al estado actual del Contexto.
    """
    def __init__(self, state: State) -> None:
        self.transition_to(state)
    
    def transition_to(self, state: State):
        """
        El Contexto permite cambiar el objeto Estado en tiempo de ejecución.
        """
        print(f"Contexto: Transición a {type(state).__name__}")
        self._state = state
        self._state.context = self
    
    """
    El Contexto delega parte de su comportamiento al objeto Estado actual.
    """
    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()

class State(ABC):
    """
    La clase base Estado declara los métodos que todos los Estados Concretos deben
    implementar y también proporciona una referencia al objeto Contexto,
    asociado con el Estado. Esta referencia se puede utilizar por los Estados para
    cambiar el Contexto a otro Estado.
    """
    @property
    def context(self) -> Context:
        return self._context
    
    @context.setter
    def context(self, context: Context) -> None:
        self._context = context
    
    @abstractmethod
    def handle1(self) -> None:
        pass
    
    @abstractmethod
    def handle2(self) -> None:
        pass

"""
Los Estados Concretos implementan varios comportamientos asociados con un estado del
Contexto.
"""
class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA maneja la solicitud1.")
        print("ConcreteStateA quiere cambiar el estado del contexto.")
        self.context.transition_to(ConcreteStateB())
    
    def handle2(self) -> None:
        print("ConcreteStateA maneja la solicitud2.")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB maneja la solicitud1.")

    def handle2(self) -> None:
        print("ConcreteStateB maneja la solicitud2.")
        print("ConcreteStateB quiere cambiar el estado del contexto.")
        self.context.transition_to(ConcreteStateA())

if __name__ == "__main__":
    # Código del cliente.
    contexto = Context(ConcreteStateA())
    contexto.request1()
    contexto.request2()