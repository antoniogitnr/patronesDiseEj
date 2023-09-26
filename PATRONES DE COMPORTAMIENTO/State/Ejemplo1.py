from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def do_action(self):
        pass

class ConcreteStateA(State):
    def do_action(self):
        print("Ejecutando acción en Estado A")

class ConcreteStateB(State):
    def do_action(self):
        print("Ejecutando acción en Estado B")

class Context:
    def __init__(self):
        self.state = None
    
    def set_state(self, state):
        self.state = state
    
    def execute_action(self):
        self.state.do_action()

# Uso del patrón State
contexto = Context()

estado_a = ConcreteStateA()
contexto.set_state(estado_a)
contexto.execute_action()

estado_b = ConcreteStateB()
contexto.set_state(estado_b)
contexto.execute_action()