from abc import ABC, abstractmethod

# Componente
class Caja(ABC):
    @abstractmethod
    def abrir(self):
        pass

# Hoja
class Computador(Caja):
    def abrir(self):
        print("Abriendo la caja del computador")

class TV(Caja):
    def abrir(self):
        print("Abriendo la caja del TV")

class Celular(Caja):
    def abrir(self):
        print("Abriendo la caja del celular")

# Compuesto
class CajaCompuesta(Caja):
    def __init__(self):
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def abrir(self):
        print("Abriendo la caja compuesta")
        for componente in self.componentes:
            componente.abrir()

# Uso del patrón Composite
if __name__ == "__main__":
    caja_principal = CajaCompuesta()
    caja_principal.agregar(Computador())
    caja_principal.agregar(TV())

    caja_secundaria = CajaCompuesta()
    caja_secundaria.agregar(Celular())

    caja_principal.agregar(caja_secundaria)

    caja_principal.abrir()