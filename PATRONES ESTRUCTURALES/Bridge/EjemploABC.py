from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraccion:
    """
    La Abstracción define la interfaz para la parte "control" de las dos jerarquías de clases.
    Mantiene una referencia a un objeto de la jerarquía de Implementación y delega todo el trabajo real a este objeto.
    """

    def __init__(self, implementacion: Implementacion) -> None:
        self.implementacion = implementacion

    def operacion(self) -> str:
        return (f"Abstraccion: Operación base con:\n"
                f"{self.implementacion.operacion_implementacion()}")

class AbstraccionExtendida(Abstraccion):
    """
    Puedes extender la Abstracción sin cambiar las clases de Implementación.
    """

    def operacion(self) -> str:
        return (f"AbstraccionExtendida: Operación extendida con:\n"
                f"{self.implementacion.operacion_implementacion()}")

class Implementacion(ABC):
    """
    La Implementación define la interfaz para todas las clases de implementación. No tiene que coincidir con la interfaz de la Abstracción.
    De hecho, las dos interfaces pueden ser completamente diferentes. 
    Normalmente, la interfaz de Implementación solo proporciona operaciones primitivas, mientras que la Abstracción define operaciones de nivel superior basadas en esas primitivas.
    """

    @abstractmethod
    def operacion_implementacion(self) -> str:
        pass

"""
Cada Implementación Concreta corresponde a una plataforma específica e implementa la interfaz de Implementación utilizando la API de esa plataforma.
"""

class ImplementacionConcretaA(Implementacion):
    def operacion_implementacion(self) -> str:
        return "ImplementacionConcretaA: Aquí está el resultado en la plataforma A."

class ImplementacionConcretaB(Implementacion):
    def operacion_implementacion(self) -> str:
        return "ImplementacionConcretaB: Aquí está el resultado en la plataforma B."

def codigo_cliente(abstraccion: Abstraccion) -> None:
    """
    Excepto en la fase de inicialización, donde un objeto Abstraccion se vincula a un objeto de Implementación específico,
    el código del cliente solo debe depender de la clase Abstraccion.
    De esta manera, el código del cliente puede admitir cualquier combinación de abstracción-implementación.
    """
    # ...
    print(abstraccion.operacion(), end="")
    # ...

if __name__ == "__main__":
    """
    El código del cliente debería poder funcionar con cualquier combinación de abstracción-implementación preconfigurada.
    """
    implementacion = ImplementacionConcretaA()
    abstraccion = Abstraccion(implementacion)
    codigo_cliente(abstraccion)
    print("\n")
    implementacion = ImplementacionConcretaB()
    abstraccion = AbstraccionExtendida(implementacion)
    codigo_cliente(abstraccion)