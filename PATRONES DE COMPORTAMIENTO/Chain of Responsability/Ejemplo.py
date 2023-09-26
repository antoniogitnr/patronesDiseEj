from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    La interfaz Handler declara un método para construir la cadena de manejadores.
    También declara un método para ejecutar una solicitud.
    """
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass
    
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    """
    El comportamiento de encadenamiento predeterminado puede implementarse dentro de una clase base de manejador.
    """
    _next_handler: Handler = None
    
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Devolver un manejador desde aquí nos permitirá enlazar los manejadores de una manera conveniente como esta:
        # monkey.set_next(squirrel).set_next(dog)
        return handler
    
    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

"""
Todos los manejadores concretos manejan una solicitud o la pasan al siguiente manejador en la cadena.
"""
class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Mono: Voy a comerme la {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Ardilla: Voy a comerme la {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Perro: Voy a comerme la {request}"
        else:
            return super().handle(request)

def client_code(handler: Handler) -> None:
    """
    El código del cliente generalmente está diseñado para funcionar con un solo manejador. En la mayoría de los casos,
    ni siquiera es consciente de que el manejador es parte de una cadena.
    """
    for food in ["Nut", "Banana", "Taza de café"]:
        print(f"\nCliente: ¿Quién quiere {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} quedó intacto.", end="")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)
    # El cliente debería poder enviar una solicitud a cualquier manejador, no solo al primero en la cadena.
    print("Cadena: Mono > Ardilla > Perro")
    client_code(monkey)
    print("\n")
    print("Subcadena: Ardilla > Perro")
    client_code(squirrel)
    print("\n")
    print('Subcadena: Perro ')
    client_code(dog)    