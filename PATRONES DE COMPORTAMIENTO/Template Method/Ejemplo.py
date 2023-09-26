from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """
    La Clase Abstracta define un método de plantilla que contiene el esqueleto de
    un algoritmo, compuesto por llamadas a operaciones primitivas (generalmente abstractas).
    Las subclases concretas deben implementar estas operaciones, pero dejar el
    método de plantilla intacto.
    """
    def template_method(self) -> None:
        """
        El método de plantilla define el esqueleto de un algoritmo.
        """
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()
    
    # Estas operaciones ya tienen implementaciones.
    def base_operation1(self) -> None:
        print("La Clase Abstracta dice: Estoy realizando la mayor parte del trabajo")
    
    def base_operation2(self) -> None:
        print("La Clase Abstracta dice: Pero permito que las subclases anulen algunas operaciones")
    
    def base_operation3(self) -> None:
        print("La Clase Abstracta dice: Pero de todos modos estoy realizando la mayor parte del trabajo")
    
    # Estas operaciones deben ser implementadas en las subclases.
    @abstractmethod
    def required_operations1(self) -> None:
        pass
    
    @abstractmethod
    def required_operations2(self) -> None:
        pass
    
    # Estos son "hooks". Las subclases pueden anularlos, pero no es obligatorio
    # ya que los hooks ya tienen una implementación predeterminada (pero vacía).
    # Los hooks proporcionan puntos de extensión adicionales en lugares cruciales del algoritmo.
    def hook1(self) -> None:
        pass
    
    def hook2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    """
    Las clases concretas deben implementar todas las operaciones abstractas de la clase base.
    También pueden anular algunas operaciones con una implementación predeterminada.
    """
    def required_operations1(self) -> None:
        print("ConcreteClass1 dice: Operación1 implementada")
    
    def required_operations2(self) -> None:
        print("ConcreteClass1 dice: Operación2 implementada")

class ConcreteClass2(AbstractClass):
    """
    Por lo general, las clases concretas solo anulan una fracción de las operaciones de la clase base.
    """
    def required_operations1(self) -> None:
        print("ConcreteClass2 dice: Operación1 implementada")
    
    def required_operations2(self) -> None:
        print("ConcreteClass2 dice: Operación2 implementada")
    
    def hook1(self) -> None:
        print("ConcreteClass2 dice: Hook1 sobreescrito")

def client_code(abstract_class: AbstractClass) -> None:
    """
    El código del cliente llama al método de plantilla para ejecutar el algoritmo.
    El código del cliente no tiene que conocer la clase concreta de un objeto con el que trabaja,
    siempre y cuando trabaje con objetos a través de la interfaz de su clase base.
    """
    # ...
    abstract_class.template_method()
    # ...

if __name__ == "__main__":
    print("El mismo código del cliente puede funcionar con diferentes subclases:")
    client_code(ConcreteClass1())
    print("")
    print("El mismo código del cliente puede funcionar con diferentes subclases:")
    client_code(ConcreteClass2())