from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """
    La clase abstracta define el método de plantilla que contiene la estructura del algoritmo.
    """
    def template_method(self) -> None:
        self.step1()
        self.step2()
        self.step3()

    @abstractmethod
    def step1(self) -> None:
        pass

    @abstractmethod
    def step2(self) -> None:
        pass

    @abstractmethod
    def step3(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    """
    Las subclases concretas implementan los pasos específicos del algoritmo.
    """
    def step1(self) -> None:
        print("Paso 1 de ConcreteClass1")

    def step2(self) -> None:
        print("Paso 2 de ConcreteClass1")

    def step3(self) -> None:
        print("Paso 3 de ConcreteClass1")

class ConcreteClass2(AbstractClass):
    """
    Otras subclases concretas pueden implementar los pasos de manera diferente.
    """
    def step1(self) -> None:
        print("Paso 1 de ConcreteClass2")

    def step2(self) -> None:
        print("Paso 2 de ConcreteClass2")

    def step3(self) -> None:
        print("Paso 3 de ConcreteClass2")

if __name__ == "__main__":
    print("Ejemplo del patrón de diseño Template Method:")
    print("Usando ConcreteClass1:")
    concrete_class1 = ConcreteClass1()
    concrete_class1.template_method()

    print("\nUsando ConcreteClass2:")
    concrete_class2 = ConcreteClass2()
    concrete_class2.template_method()