from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

"""
Para crear un iterador en Python, existen dos clases abstractas del módulo incorporado  `collections`  - Iterable, Iterator. Necesitamos implementar el método  `__iter__()`  en el objeto iterado (colección) y el método  `__next__()`  en el iterador.
"""

class AlphabeticalOrderIterator(Iterator):
    """
    Los Iteradores concretos implementan varios algoritmos de recorrido. Estas clases
    almacenan la posición actual del recorrido en todo momento.
    """

    """
    El atributo  `_position`  almacena la posición actual del recorrido. Un iterador puede
    tener muchos otros campos para almacenar el estado de la iteración, especialmente cuando se
    supone que debe funcionar con un tipo particular de colección.
    """
    _position: int = None

    """
    Este atributo indica la dirección del recorrido.
    """
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        El método __next__() debe devolver el siguiente elemento de la secuencia. Al
        llegar al final, y en llamadas posteriores, debe generar StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

class WordsCollection(Iterable):
    """
    Las Colecciones concretas proporcionan uno o varios métodos para obtener nuevas
    instancias de iteradores, compatibles con la clase de la colección.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        El método __iter__() devuelve el objeto iterador en sí mismo, por defecto lo
        devolvemos en orden ascendente.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)

if __name__ == "__main__":
    # El código del cliente puede o no conocer las clases Iterador o Colección concretas,
    # dependiendo del nivel de abstracción que se desee mantener en el programa.
    collection = WordsCollection()
    collection.add_item("Primero")
    collection.add_item("Segundo")
    collection.add_item("Tercero")
    print("Recorrido directo:")
    print("\n".join(collection))
    print("")
    print("Recorrido inverso:")
    print("\n".join(collection.get_reverse_iterator()), end="")