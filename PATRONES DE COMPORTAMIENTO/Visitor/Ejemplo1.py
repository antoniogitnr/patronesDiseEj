from abc import ABC, abstractmethod

# Componente
class Elemento(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Componente Concreto A
class ElementoA(Elemento):
    def accept(self, visitor):
        visitor.visit_elemento_a(self)

    def operation_a(self):
        return "Operación A"

# Componente Concreto B
class ElementoB(Elemento):
    def accept(self, visitor):
        visitor.visit_elemento_b(self)

    def operation_b(self):
        return "Operación B"

# Visitor
class Visitor(ABC):
    @abstractmethod
    def visit_elemento_a(self, elemento_a):
        pass

    @abstractmethod
    def visit_elemento_b(self, elemento_b):
        pass

# Visitor Concreto
class VisitorConcreto(Visitor):
    def visit_elemento_a(self, elemento_a):
        print(f"Realizando operación en {elemento_a.operation_a()}")

    def visit_elemento_b(self, elemento_b):
        print(f"Realizando operación en {elemento_b.operation_b()}")

# Cliente
elementos = [ElementoA(), ElementoB()]
visitor = VisitorConcreto()

for elemento in elementos:
    elemento.accept(visitor)