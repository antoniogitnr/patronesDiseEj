from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):
    """
    La clase Componente base declara operaciones comunes tanto para objetos
    simples como complejos de una composición.
    """

    @property
    def padre(self) -> Componente:
        return self._padre

    @padre.setter
    def padre(self, padre: Componente):
        """
        Opcionalmente, el Componente base puede declarar una interfaz para establecer
        y acceder a un padre del componente en una estructura de árbol. También puede
        proporcionar alguna implementación predeterminada para estos métodos.
        """
        self._padre = padre

    """
    En algunos casos, sería beneficioso definir las operaciones de gestión de hijos
    directamente en la clase Componente base. De esta manera, no será necesario exponer
    ninguna clase de componente concreto al código del cliente, incluso durante el
    ensamblaje del árbol de objetos. La desventaja es que estos métodos estarán vacíos
    para los componentes de nivel hoja.
    """

    def agregar(self, componente: Componente) -> None:
        pass

    def eliminar(self, componente: Componente) -> None:
        pass

    def es_compuesto(self) -> bool:
        """
        Puede proporcionar un método que permita al código del cliente determinar si
        un componente puede tener hijos.
        """
        return False

    @abstractmethod
    def operacion(self) -> str:
        """
        El Componente base puede implementar un comportamiento predeterminado o
        dejarlo a las clases concretas (declarando el método que contiene el
        comportamiento como "abstracto").
        """
        pass

class Hoja(Componente):
    """
    La clase Hoja representa los objetos finales de una composición. Una hoja no
    puede tener hijos. Por lo general, son las hojas las que realizan el trabajo
    real, mientras que los objetos Compuesto solo delegan a sus subcomponentes.
    """

    def operacion(self) -> str:
        return "Hoja"

class Compuesto(Componente):
    """
    La clase Compuesto representa los componentes complejos que pueden tener hijos.
    Por lo general, los objetos Compuesto delegan el trabajo real a sus hijos y luego
    "resumen" el resultado.
    """

    def __init__(self) -> None:
        self._hijos: List[Componente] = []

    """
    Un objeto compuesto puede agregar o eliminar otros componentes (tanto simples
    como complejos) de su lista de hijos.
    """

    def agregar(self, componente: Componente) -> None:
        self._hijos.append(componente)
        componente.padre = self

    def eliminar(self, componente: Componente) -> None:
        self._hijos.remove(componente)
        componente.padre = None

    def es_compuesto(self) -> bool:
        return True

    def operacion(self) -> str:
        """
        El Compuesto ejecuta su lógica principal de una manera particular. Recorre
        recursivamente a través de todos sus hijos, recopilando y sumando sus resultados.
        Dado que los hijos del compuesto pasan estas llamadas a sus hijos y así sucesivamente,
        se recorre todo el árbol de objetos como resultado.
        """
        resultados = []
        for hijo in self._hijos:
            resultados.append(hijo.operacion())
        return f"Rama({'+'.join(resultados)})"

def codigo_cliente(componente: Componente) -> None:
    """
    El código del cliente trabaja con todos los componentes a través de la interfaz base.
    """
    print(f"RESULTADO: {componente.operacion()}", end="")

def codigo_cliente2(componente1: Componente, componente2: Componente) -> None:
    """
    Gracias al hecho de que las operaciones de gestión de hijos se declaran en la clase
    Componente base, el código del cliente puede trabajar con cualquier componente,
    simple o complejo, sin depender de sus clases concretas.
    """
    if componente1.es_compuesto():
        componente1.agregar(componente2)
    print(f"RESULTADO: {componente1.operacion()}", end="")

if __name__ == "__main__":
    # De esta manera, el código del cliente puede trabajar con componentes simples...
    simple = Hoja()
    print("Cliente: Tengo un componente simple:")
    codigo_cliente(simple)
    print("\n")
    # ...así como con composites complejos.
    arbol = Compuesto()
    rama1 = Compuesto()
    rama1.agregar(Hoja())
    rama1.agregar(Hoja())
    rama2 = Compuesto()
    rama2.agregar(Hoja())
    arbol.agregar(rama1)
    arbol.agregar(rama2)
    print("Cliente: Ahora tengo un árbol compuesto:")
    codigo_cliente(arbol)
    print("\n")
    print("Cliente: No necesito verificar las clases de los componentes incluso al manejar el árbol:")
    codigo_cliente2(arbol, simple)