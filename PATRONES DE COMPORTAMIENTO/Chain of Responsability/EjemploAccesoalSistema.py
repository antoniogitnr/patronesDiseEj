from abc import ABC, abstractmethod

class Handler(ABC):
    """
    La interfaz Handler declara un método para manejar las solicitudes y otro método para establecer el siguiente
    manejador en la cadena.
    """
    @abstractmethod
    def manejar_solicitud(self, usuario: str, pedido: str) -> None:
        pass

    @abstractmethod
    def establecer_siguiente_manejador(self, manejador) -> None:
        pass

class AutenticacionHandler(Handler):
    def __init__(self):
        self._siguiente_manejador = None

    def manejar_solicitud(self, usuario: str, pedido: str) -> None:
        if self._autenticado(usuario):
            print(f"Pedido generado por el usuario {usuario}: {pedido}")
        elif self._siguiente_manejador is not None:
            self._siguiente_manejador.manejar_solicitud(usuario, pedido)
        else:
            print("Acceso denegado. Usuario no autenticado.")

    def establecer_siguiente_manejador(self, manejador) -> None:
        self._siguiente_manejador = manejador

    def _autenticado(self, usuario: str) -> bool:
        # Aquí se realizaría la lógica de autenticación real, como verificar las credenciales en una base de datos
        # En este ejemplo, se asume que el usuario está autenticado si no está vacío
        return bool(usuario)

class GenerarPedidoHandler(Handler):
    def __init__(self):
        self._siguiente_manejador = None

    def manejar_solicitud(self, usuario: str, pedido: str) -> None:
        if pedido:
            print(f"Pedido generado por el usuario {usuario}: {pedido}")
        elif self._siguiente_manejador is not None:
            self._siguiente_manejador.manejar_solicitud(usuario, pedido)
        else:
            print("No se puede generar un pedido vacío.")

    def establecer_siguiente_manejador(self, manejador) -> None:
        self._siguiente_manejador = manejador

if __name__ == "__main__":
    autenticacion_handler = AutenticacionHandler()
    generar_pedido_handler = GenerarPedidoHandler()
    autenticacion_handler.establecer_siguiente_manejador(generar_pedido_handler)

    # Intentar generar un pedido sin autenticación
    autenticacion_handler.manejar_solicitud("", "Pedido 1")

    # Autenticar al usuario
    autenticado = autenticacion_handler.manejar_solicitud("usuario1", "")

    # Generar un pedido autenticado
    if autenticado:
        autenticacion_handler.manejar_solicitud("usuario1", "Pedido 2")