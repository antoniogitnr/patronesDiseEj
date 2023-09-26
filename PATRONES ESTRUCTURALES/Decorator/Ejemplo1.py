# Clase base Componente
class Componente:
    def operacion(self) -> str:
        pass

# Clase concreta que implementa Componente
class ComponenteConcreto(Componente):
    def operacion(self) -> str:
        return "Componente Concreto"

# Clase base Decorador
class Decorador(Componente):
    def __init__(self, componente: Componente):
        self.componente = componente

    def operacion(self) -> str:
        return self.componente.operacion()

# Decorador concreto que agrega funcionalidad adicional
class DecoradorA(Decorador):
    def operacion(self) -> str:
        return f"Funcionalidad adicional A\n{self.componente.operacion()}"

# Decorador concreto que agrega otra funcionalidad adicional
class DecoradorB(Decorador):
    def operacion(self) -> str:
        return f"Funcionalidad adicional B\n{self.componente.operacion()}"

# Uso del patrón Decorator
componente = ComponenteConcreto()
decorador1 = DecoradorA(componente)
decorador2 = DecoradorB(decorador1)

print(decorador2.operacion())