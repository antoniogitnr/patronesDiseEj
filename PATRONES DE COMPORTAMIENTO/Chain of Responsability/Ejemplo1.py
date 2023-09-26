from abc import ABC, abstractmethod

class Handler(ABC):
    """
    La interfaz Handler declara un método para manejar las solicitudes y otro método para establecer el siguiente
    manejador en la cadena.
    """
    @abstractmethod
    def manejar_solicitud(self, solicitud: str) -> None:
        pass

    @abstractmethod
    def establecer_siguiente_manejador(self, manejador) -> None:
        pass

class ManejadorConcretoA(Handler):
    def __init__(self):
        self._siguiente_manejador = None

    def manejar_solicitud(self, solicitud: str) -> None:
        if solicitud == "A":
            print("ManejadorConcretoA maneja la solicitud.")
        elif self._siguiente_manejador is not None:
            self._siguiente_manejador.manejar_solicitud(solicitud)
        else:
            print("Ningún manejador puede manejar la solicitud.")

    def establecer_siguiente_manejador(self, manejador) -> None:
        self._siguiente_manejador = manejador

class ManejadorConcretoB(Handler):
    def __init__(self):
        self._siguiente_manejador = None

    def manejar_solicitud(self, solicitud: str) -> None:
        if solicitud == "B":
            print("ManejadorConcretoB maneja la solicitud.")
        elif self._siguiente_manejador is not None:
            self._siguiente_manejador.manejar_solicitud(solicitud)
        else:
            print("Ningún manejador puede manejar la solicitud.")

    def establecer_siguiente_manejador(self, manejador) -> None:
        self._siguiente_manejador = manejador

if __name__ == "__main__":
    manejador_a = ManejadorConcretoA()
    manejador_b = ManejadorConcretoB()
    manejador_a.establecer_siguiente_manejador(manejador_b)

    # La solicitud se envía al primer manejador de la cadena
    manejador_a.manejar_solicitud("A")
    print("---")

    # La solicitud se envía al segundo manejador de la cadena
    manejador_a.manejar_solicitud("B")
    print("---")

    # La solicitud no puede ser manejada por ninguno de los manejadores en la cadena
    manejador_a.manejar_solicitud("C")