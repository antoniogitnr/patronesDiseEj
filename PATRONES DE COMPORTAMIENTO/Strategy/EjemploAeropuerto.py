from abc import ABC, abstractmethod

# Interfaz de estrategia
class EstrategiaTransporte(ABC):
    @abstractmethod
    def llegar_al_aeropuerto(self):
        pass

# Estrategia concreta para llegar en bicicleta
class LlegarEnBicicleta(EstrategiaTransporte):
    def llegar_al_aeropuerto(self):
        print("Llegando al aeropuerto en bicicleta")

# Estrategia concreta para llegar en moto
class LlegarEnMoto(EstrategiaTransporte):
    def llegar_al_aeropuerto(self):
        print("Llegando al aeropuerto en moto")

# Estrategia concreta para llegar en carro
class LlegarEnCarro(EstrategiaTransporte):
    def llegar_al_aeropuerto(self):
        print("Llegando al aeropuerto en carro")

# Estrategia concreta para llegar en bus
class LlegarEnBus(EstrategiaTransporte):
    def llegar_al_aeropuerto(self):
        print("Llegando al aeropuerto en bus")

# Contexto
class ViajeAlAeropuerto:
    def __init__(self, estrategia: EstrategiaTransporte):
        self._estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaTransporte):
        self._estrategia = estrategia

    def viajar(self):
        self._estrategia.llegar_al_aeropuerto()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear el contexto y establecer la estrategia inicial
    viaje = ViajeAlAeropuerto(LlegarEnBicicleta())

    # Realizar el viaje
    viaje.viajar()

    # Cambiar la estrategia a llegar en carro
    viaje.cambiar_estrategia(LlegarEnCarro())

    # Realizar el viaje nuevamente con la nueva estrategia
    viaje.viajar()