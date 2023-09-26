class Component():
    """
    La interfaz base Component define las operaciones que pueden ser alteradas por
    los decoradores.
    """
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    """
    Los Componentes Concretos proporcionan implementaciones predeterminadas de las operaciones. 
    Puede haber varias variaciones de estas clases.
    """
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    """
    La clase base Decorator sigue la misma interfaz que los otros componentes.
    El propósito principal de esta clase es definir la interfaz de envoltura para
    todos los decoradores concretos. La implementación predeterminada del código de envoltura
    podría incluir un campo para almacenar un componente envuelto y los medios para
    inicializarlo.
    """
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        El Decorador delega todo el trabajo al componente envuelto.
        """
        return self._component

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    """
    Los Decoradores Concretos llaman al objeto envuelto y alteran su resultado de alguna
    manera.
    """
    def operation(self) -> str:
        """
        Los decoradores pueden llamar a la implementación principal de la operación en lugar de
        llamar directamente al objeto envuelto. Este enfoque simplifica la extensión
        de las clases de decoradores.
        """
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    """
    Los decoradores pueden ejecutar su comportamiento antes o después de la llamada a un
    objeto envuelto.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component: Component) -> None:
    """
    El código del cliente trabaja con todos los objetos utilizando la interfaz Component. De esta
    manera, puede mantenerse independiente de las clases concretas de componentes con las que trabaja.
    """
    # ...
    print(f"RESULTADO: {component.operation()}", end="")
    # ...

if __name__ == "__main__":
    # De esta manera, el código del cliente puede admitir tanto componentes simples...
    simple = ConcreteComponent()
    print("Cliente: Tengo un componente simple:")
    client_code(simple)
    print("\n")
    # ...como componentes decorados.
    #
    # Observa cómo los decoradores pueden envolver no solo componentes simples, sino también
    # otros decoradores.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Cliente: Ahora tengo un componente decorado:")
    client_code(decorator2)