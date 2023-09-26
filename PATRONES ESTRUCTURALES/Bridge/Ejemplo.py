from abc import ABC, abstractmethod

# Clase de abstracción
class Abstraccion:
    def __init__(self, implementacion):
        self.implementacion = implementacion

    def operacion(self):
        return self.implementacion.realizar_operacion()

# Clase de implementación
class Implementacion(ABC):
    @abstractmethod
    def realizar_operacion(self):
        pass

# Implementación concreta A
class ImplementacionConcretaA(Implementacion):
    def realizar_operacion(self):
        return "ImplementacionConcretaA: Operación realizada."

# Implementación concreta B
class ImplementacionConcretaB(Implementacion):
    def realizar_operacion(self):
        return "ImplementacionConcretaB: Operación realizada."

# Cliente
if __name__ == "__main__":
    implementacion_a = ImplementacionConcretaA()
    abstraccion_a = Abstraccion(implementacion_a)
    print(abstraccion_a.operacion())

    implementacion_b = ImplementacionConcretaB()
    abstraccion_b = Abstraccion(implementacion_b)
    print(abstraccion_b.operacion())