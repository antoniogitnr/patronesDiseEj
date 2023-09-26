import json
from typing import Dict

class Flyweight():
    """
    El Flyweight almacena una porción común del estado (también llamado estado
    intrínseco) que pertenece a múltiples entidades comerciales reales. El
    Flyweight acepta el resto del estado (estado extrínseco, único para cada
    entidad) a través de los parámetros de su método.
    """
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Mostrando estado compartido ({s}) y único ({u}).", end="")

class FlyweightFactory():
    """
    La Fábrica de Flyweights crea y gestiona los objetos Flyweight. Asegura que
    los flyweights se compartan correctamente. Cuando el cliente solicita un
    flyweight, la fábrica devuelve una instancia existente o crea una nueva, si
    aún no existe.
    """
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        Devuelve el hash de cadena de un Flyweight para un estado dado.
        """
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        Devuelve un Flyweight existente con un estado dado o crea uno nuevo.
        """
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print("FlyweightFactory: No se puede encontrar un flyweight, creando uno nuevo.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reutilizando flyweight existente.")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: Tengo {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")

def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nCliente: Agregando un auto a la base de datos.")
    flyweight = factory.get_flyweight([brand, model, color])
    # El código del cliente almacena o calcula el estado extrínseco y lo pasa
    # a los métodos del flyweight.
    flyweight.operation([plates, owner])

if __name__ == "__main__":
    """
    El código del cliente generalmente crea un montón de flyweights prellenados en la
    etapa de inicialización de la aplicación.
    """
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "rosado"],
        ["Mercedes Benz", "C300", "negro"],
        ["Mercedes Benz", "C500", "rojo"],
        ["BMW", "M5", "rojo"],
        ["BMW", "X6", "blanco"],
    ])
    factory.list_flyweights()
    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "rojo")
    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "rojo")
    print("\n")
    factory.list_flyweights()