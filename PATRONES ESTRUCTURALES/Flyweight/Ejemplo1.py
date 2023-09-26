from typing import Dict

class Flyweight:
    def __init__(self, estado_compartido: str) -> None:
        self._estado_compartido = estado_compartido

    def operacion(self, estado_unico: str) -> None:
        print(f"Flyweight: Mostrando estado compartido ({self._estado_compartido}) y estado único ({estado_unico}).")

class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def obtener_flyweight(self, estado_compartido: str) -> Flyweight:
        if estado_compartido not in self._flyweights:
            self._flyweights[estado_compartido] = Flyweight(estado_compartido)
        return self._flyweights[estado_compartido]

def main():
    fabrica = FlyweightFactory()

    flyweight1 = fabrica.obtener_flyweight("Estado Compartido 1")
    flyweight1.operacion("Estado Único 1")

    flyweight2 = fabrica.obtener_flyweight("Estado Compartido 2")
    flyweight2.operacion("Estado Único 2")

    flyweight3 = fabrica.obtener_flyweight("Estado Compartido 1")
    flyweight3.operacion("Estado Único 3")

if __name__ == "__main__":
    main()