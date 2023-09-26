# Clase base Componente
class Notificacion:
    def enviar(self) -> str:
        pass

# Clase concreta que implementa Componente
class NotificacionBasica(Notificacion):
    def enviar(self) -> str:
        return "Notificación básica enviada"

# Clase base Decorador
class DecoradorNotificacion(Notificacion):
    def __init__(self, notificacion: Notificacion):
        self.notificacion = notificacion

    def enviar(self) -> str:
        return self.notificacion.enviar()

# Decorador concreto que agrega funcionalidad adicional
class DecoradorNotificacionSonido(DecoradorNotificacion):
    def enviar(self) -> str:
        return f"Notificación con sonido\n{self.notificacion.enviar()}"

# Decorador concreto que agrega otra funcionalidad adicional
class DecoradorNotificacionImagen(DecoradorNotificacion):
    def enviar(self) -> str:
        return f"Notificación con imagen\n{self.notificacion.enviar()}"

# Uso del patrón Decorator
notificacion = NotificacionBasica()
notificacion_con_sonido = DecoradorNotificacionSonido(notificacion)
notificacion_con_imagen = DecoradorNotificacionImagen(notificacion_con_sonido)

print(notificacion_con_imagen.enviar())