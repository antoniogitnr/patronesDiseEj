""" from _future_ import annotations """
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    La clase Creator declara el método de fábrica que se supone que debe devolver
    un objeto de la clase Product. Las subclases de Creator suelen proporcionar
    la implementación de este método.
    """
    @abstractmethod
    def factory_method(self):
        """
        Tenga en cuenta que el Creator también puede proporcionar una implementación
        predeterminada del método de fábrica.
        """
        pass

    def some_operation(self) -> str:
        """
        También tenga en cuenta que, a pesar de su nombre, la responsabilidad principal
        del Creator no es crear productos. Por lo general, contiene lógica empresarial
        central que depende de los objetos Product devueltos por el método de fábrica.
        Las subclases pueden cambiar indirectamente esa lógica empresarial sobrescribiendo
        el método de fábrica y devolviendo un tipo de producto diferente.
        """
        # Llama al método de fábrica para crear un objeto Product.
        product = self.factory_method()
        # Ahora, usa el producto.
        result = f"Creador: El mismo código del creador acaba de funcionar con {product.operation()}"
        return result

class Product(ABC):
    """
    La interfaz Product declara las operaciones que todos los productos concretos deben implementar.
    """
    @abstractmethod
    def operation(self) -> str:
        pass

"""
Los creadores concretos sobrescriben el método de fábrica para cambiar el tipo de producto resultante.
"""
class ConcreteCreator1(Creator):
    """
    Tenga en cuenta que la firma del método aún utiliza el tipo de producto abstracto,
    aunque el producto concreto se devuelve realmente desde el método. De esta manera,
    el Creator puede mantenerse independiente de las clases de producto concretas.
    """
    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()



"""
Los productos concretos proporcionan varias implementaciones de la interfaz Product.
"""
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado del ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado del ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    """
    El código del cliente funciona con una instancia de un creador concreto, aunque
    a través de su interfaz base. Mientras el cliente siga trabajando con el creador
    a través de la interfaz base, se le puede pasar cualquier subclase del creador.
    """
    print(f"Cliente: No conozco la clase del creador, pero aún funciona.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("Aplicación: Iniciada con ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")
    print("Aplicación: Iniciada con ConcreteCreator2.")
    client_code(ConcreteCreator2())



""" RESULTADOS:

Aplicación: Iniciada con ConcreteCreator1.
Cliente: No conozco la clase del creador, pero aún funciona.
Creador: El mismo código del creador acaba de funcionar con {Resultado del ConcreteProduct1}

Aplicación: Iniciada con ConcreteCreator2.
Cliente: No conozco la clase del creador, pero aún funciona.
Creador: El mismo código del creador acaba de funcionar con {Resultado del ConcreteProduct2}
"""