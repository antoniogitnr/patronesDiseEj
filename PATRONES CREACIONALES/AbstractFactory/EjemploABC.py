from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """
    La interfaz Abstract Factory declara un conjunto de métodos que devuelven
    diferentes productos abstractos. Estos productos se llaman familia y están
    relacionados por un tema o concepto de alto nivel. Los productos de una familia
    suelen poder colaborar entre sí. Una familia de productos puede tener varias
    variantes, pero los productos de una variante son incompatibles con los productos de
    otra.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Las Fábricas Concretas producen una familia de productos que pertenecen a una sola
    variante. La fábrica garantiza que los productos resultantes sean compatibles. 
    Tenga en cuenta que las firmas de los métodos de la Fábrica Concreta devuelven un
    producto abstracto, mientras que dentro del método se instancia un producto concreto.
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Cada Fábrica Concreta tiene una variante de producto correspondiente.
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Cada producto distinto de una familia de productos debe tener una interfaz base.
    Todas las variantes del producto deben implementar esta interfaz.
    """
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado del producto A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado del producto A2."


class AbstractProductB(ABC):
    """
    Aquí está la interfaz base de otro producto. Todos los productos pueden interactuar
    entre sí, pero la interacción adecuada solo es posible entre productos de la misma
    variante concreta.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado del producto B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"El resultado del B1 colaborando con el ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado del producto B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"El resultado del B2 colaborando con el ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    El código del cliente trabaja con fábricas y productos solo a través de tipos abstractos:
    AbstractFactory y AbstractProduct. Esto permite pasar cualquier subclase de fábrica o
    producto al código del cliente sin romperlo.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    El código del cliente puede trabajar con cualquier clase de fábrica concreta.
    """
    print("Cliente: Probando el código del cliente con el primer tipo de fábrica:")
    client_code(ConcreteFactory1())
    print("\n")
    print("Cliente: Probando el mismo código del cliente con el segundo tipo de fábrica:")
    client_code(ConcreteFactory2())