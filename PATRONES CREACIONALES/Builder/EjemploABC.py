from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """
    La interfaz Builder especifica los métodos para crear las diferentes partes
    de los objetos Producto.
    """
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass

class ConcreteBuilder1(Builder):
    """
    Las clases ConcreteBuilder siguen la interfaz Builder y proporcionan
    implementaciones específicas de los pasos de construcción. Tu programa puede
    tener varias variaciones de Builders implementadas de manera diferente.
    """
    def __init__(self) -> None:
        """
        Una nueva instancia de builder debería contener un objeto Producto en
        blanco, que se utiliza en el ensamblaje posterior.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Los Builders concretos deben proporcionar sus propios métodos para
        obtener resultados. Esto se debe a que varios tipos de builders pueden
        crear productos completamente diferentes que no siguen la misma
        interfaz. Por lo tanto, estos métodos no pueden declararse en la
        interfaz Builder base (al menos en un lenguaje de programación
        estáticamente tipado). Por lo general, después de devolver el resultado
        final al cliente, se espera que una instancia de builder esté lista para
        comenzar a producir otro producto. Por eso es una práctica habitual
        llamar al método reset al final del cuerpo del método getProduct. Sin
        embargo, este comportamiento no es obligatorio y puedes hacer que tus
        builders esperen una llamada de reset explícita desde el código del
        cliente antes de desechar el resultado anterior.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("ParteA1")

    def produce_part_b(self) -> None:
        self._product.add("ParteB1")

    def produce_part_c(self) -> None:
        self._product.add("ParteC1")

class Product1():
    """
    Tiene sentido utilizar el patrón Builder solo cuando tus productos son
    bastante complejos y requieren una configuración extensa. A diferencia de
    otros patrones de creación, los diferentes builders concretos pueden
    producir productos no relacionados. En otras palabras, los resultados de
    varios builders pueden no seguir siempre la misma interfaz.
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes del producto: {', '.join(self.parts)}", end="")

class Director:
    """
    El Director solo es responsable de ejecutar los pasos de construcción en un
    orden particular. Es útil cuando se produce productos de acuerdo con un
    orden o configuración específica. Estrictamente hablando, la clase Director
    es opcional, ya que el código del cliente puede controlar los builders
    directamente.
    """
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        El Director trabaja con cualquier instancia de builder que el código del
        cliente le pase. De esta manera, el código del cliente puede alterar el
        tipo final del producto recién ensamblado.
        """
        self._builder = builder

    """
    El Director puede construir varias variaciones del producto utilizando los
    mismos pasos de construcción.
    """
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

if __name__ == "__main__":
    """
    El código del cliente crea un objeto builder, lo pasa al director e
    inicia el proceso de construcción. El resultado final se obtiene del objeto
    builder.
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Producto básico estándar:")
    director.build_minimal_viable_product()
    builder.product.list_parts()
    print("\n")

    print("Producto completo estándar:")
    director.build_full_featured_product()
    builder.product.list_parts()
    print("\n")

    # Recuerda, el patrón Builder se puede utilizar sin una clase Director.
    print("Producto personalizado:")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()