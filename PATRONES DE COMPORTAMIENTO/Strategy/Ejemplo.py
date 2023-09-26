from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Contexto():
    """
    El Contexto define la interfaz de interés para los clientes.
    """
    def __init__(self, estrategia: Estrategia) -> None:
        """
        Normalmente, el Contexto acepta una estrategia a través del constructor, pero
        también proporciona un método setter para cambiarla en tiempo de ejecución.
        """
        self._estrategia = estrategia

    @property
    def estrategia(self) -> Estrategia:
        """
        El Contexto mantiene una referencia a uno de los objetos de Estrategia. El
        Contexto no conoce la clase concreta de una estrategia. Debe trabajar
        con todas las estrategias a través de la interfaz de Estrategia.
        """
        return self._estrategia

    @estrategia.setter
    def estrategia(self, estrategia: Estrategia) -> None:
        """
        Normalmente, el Contexto permite reemplazar un objeto de Estrategia en tiempo de ejecución.
        """
        self._estrategia = estrategia

    def hacer_algo_de_negocios(self) -> None:
        """
        El Contexto delega parte del trabajo al objeto de Estrategia en lugar de
        implementar múltiples versiones del algoritmo por sí mismo.
        """
        # ...
        print("Contexto: Ordenando datos usando la estrategia (no estoy seguro de cómo se hará)")
        resultado = self._estrategia.hacer_algoritmo(["a", "b", "c", "d", "e"])
        print(",".join(resultado))
        # ...


class Estrategia(ABC):
    """
    La interfaz de Estrategia declara operaciones comunes a todas las versiones
    soportadas de algún algoritmo.
    El Contexto utiliza esta interfaz para llamar al algoritmo definido por las
    Estrategias concretas.
    """

    @abstractmethod
    def hacer_algoritmo(self, datos: List):
        pass


"""
Las Estrategias concretas implementan el algoritmo siguiendo la interfaz de Estrategia base.
La interfaz las hace intercambiables en el Contexto.
"""

class EstrategiaConcretaA(Estrategia):
    def hacer_algoritmo(self, datos: List) -> List:
        return sorted(datos)


class EstrategiaConcretaB(Estrategia):
    def hacer_algoritmo(self, datos: List) -> List:
        return reversed(sorted(datos))


if __name__ == "__main__":
    # El código del cliente elige una estrategia concreta y la pasa al contexto.
    # El cliente debe ser consciente de las diferencias entre las estrategias para poder
    # tomar la elección correcta.
    contexto = Contexto(EstrategiaConcretaA())
    print("Cliente: La estrategia se establece en ordenamiento normal.")
    contexto.hacer_algo_de_negocios()
    print()
    print("Cliente: La estrategia se establece en ordenamiento inverso.")
    contexto.estrategia = EstrategiaConcretaB()
    contexto.hacer_algo_de_negocios()