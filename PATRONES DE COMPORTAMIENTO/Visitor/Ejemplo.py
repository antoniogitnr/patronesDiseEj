from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):
    """
    La interfaz Componente declara un método 'aceptar' que debería tomar la
    interfaz base del visitante como argumento.
    """
    @abstractmethod
    def aceptar(self, visitante: Visitante) -> None:
        pass

class ComponenteConcretoA(Componente):
    """
    Cada Componente Concreto debe implementar el método 'aceptar' de tal manera
    que llame al método del visitante correspondiente a la clase del componente.
    """
    def aceptar(self, visitante: Visitante) -> None:
        """
        Observa que estamos llamando a 'visitarComponenteConcretoA', que coincide
        con el nombre de la clase actual. De esta manera, le permitimos al visitante
        saber con qué clase de componente está trabajando.
        """
        visitante.visitar_componente_concreto_a(self)

    def metodo_exclusivo_de_componente_concreto_a(self) -> str:
        """
        Los Componentes Concretos pueden tener métodos especiales que no existen en su
        clase base o interfaz. El Visitante aún puede utilizar estos métodos ya que
        conoce la clase concreta del componente.
        """
        return "A"

class ComponenteConcretoB(Componente):
    """
    Similar aquí: visitarComponenteConcretoB => ComponenteConcretoB
    """
    def aceptar(self, visitante: Visitante) -> None:
        visitante.visitar_componente_concreto_b(self)

    def metodo_especial_de_componente_concreto_b(self) -> str:
        return "B"

class Visitante(ABC):
    """
    La interfaz Visitante declara un conjunto de métodos de visita que corresponden a
    las clases de componentes. La firma de un método de visita permite al visitante
    identificar la clase exacta del componente con el que está tratando.
    """
    @abstractmethod
    def visitar_componente_concreto_a(self, elemento: ComponenteConcretoA) -> None:
        pass

    @abstractmethod
    def visitar_componente_concreto_b(self, elemento: ComponenteConcretoB) -> None:
        pass

"""
Los Visitantes Concretos implementan varias versiones del mismo algoritmo, que pueden
trabajar con todas las clases de componentes concretos.
Puedes experimentar el mayor beneficio del patrón Visitante cuando lo usas con
una estructura de objetos compleja, como un árbol compuesto. En este caso, podría ser
útil almacenar algún estado intermedio del algoritmo mientras se ejecutan
los métodos del visitante en varios objetos de la estructura.
"""

class VisitanteConcreto1(Visitante):
    def visitar_componente_concreto_a(self, elemento) -> None:
        print(f"{elemento.metodo_exclusivo_de_componente_concreto_a()} + VisitanteConcreto1")

    def visitar_componente_concreto_b(self, elemento) -> None:
        print(f"{elemento.metodo_especial_de_componente_concreto_b()} + VisitanteConcreto1")

class VisitanteConcreto2(Visitante):
    def visitar_componente_concreto_a(self, elemento) -> None:
        print(f"{elemento.metodo_exclusivo_de_componente_concreto_a()} + VisitanteConcreto2")

    def visitar_componente_concreto_b(self, elemento) -> None:
        print(f"{elemento.metodo_especial_de_componente_concreto_b()} + VisitanteConcreto2")

def codigo_cliente(componentes: List[Componente], visitante: Visitante) -> None:
    """
    El código del cliente puede ejecutar operaciones del visitante en cualquier conjunto de elementos
    sin necesidad de conocer sus clases concretas. La operación de aceptación dirige una llamada al
    método apropiado en el objeto visitante.
    """
    # ...
    for componente in componentes:
        componente.aceptar(visitante)
    # ...

if __name__ == "__main__":
    componentes = [ComponenteConcretoA(), ComponenteConcretoB()]
    print("El código del cliente funciona con todos los visitantes a través de la interfaz base Visitante:")
    visitante1 = VisitanteConcreto1()
    codigo_cliente(componentes, visitante1)

    print("Permite que el mismo código del cliente funcione con diferentes tipos de visitantes:")
    visitante2 = VisitanteConcreto2()
    codigo_cliente(componentes, visitante2)