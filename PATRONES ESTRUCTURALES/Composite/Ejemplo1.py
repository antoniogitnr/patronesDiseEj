from abc import ABC, abstractmethod

# Componente
class Componente(ABC):
    @abstractmethod
    def operacion(self):
        pass

# Hoja
class Hoja(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def operacion(self):
        print(f"Realizando operación en la hoja {self.nombre}")

# Compuesto
class Compuesto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar(self, componente):
        self.hijos.append(componente)

    def eliminar(self, componente):
        self.hijos.remove(componente)

    def operacion(self):
        print(f"Realizando operación en el compuesto {self.nombre}")
        for hijo in self.hijos:
            hijo.operacion()

# Uso del patrón Composite
if __name__ == "__main__":
    raiz = Compuesto("Raíz")
    raiz.agregar(Hoja("Hoja 1"))
    raiz.agregar(Hoja("Hoja 2"))

    compuesto = Compuesto("Compuesto 1")
    compuesto.agregar(Hoja("Hoja 3"))
    compuesto.agregar(Hoja("Hoja 4"))

    raiz.agregar(compuesto)

    raiz.operacion()