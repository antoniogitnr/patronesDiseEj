from abc import ABC, abstractmethod

# Componente
class Comida(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Componente Concreto: Pizza
class Pizza(Comida):
    def accept(self, visitor):
        visitor.visit_pizza(self)

    def preparar_pizza(self):
        return "Preparando pizza"

# Componente Concreto: Hamburguesa
class Hamburguesa(Comida):
    def accept(self, visitor):
        visitor.visit_hamburguesa(self)

    def preparar_hamburguesa(self):
        return "Preparando hamburguesa"

# Componente Concreto: Hotdog
class Hotdog(Comida):
    def accept(self, visitor):
        visitor.visit_hotdog(self)

    def preparar_hotdog(self):
        return "Preparando hotdog"

# Visitor
class Visitor(ABC):
    @abstractmethod
    def visit_pizza(self, pizza):
        pass

    @abstractmethod
    def visit_hamburguesa(self, hamburguesa):
        pass

    @abstractmethod
    def visit_hotdog(self, hotdog):
        pass

# Visitor Concreto
class VisitorVenta(Visitor):
    def visit_pizza(self, pizza):
        print(f"Vendiendo {pizza.preparar_pizza()}")

    def visit_hamburguesa(self, hamburguesa):
        print(f"Vendiendo {hamburguesa.preparar_hamburguesa()}")

    def visit_hotdog(self, hotdog):
        print(f"Vendiendo {hotdog.preparar_hotdog()}")

# Cliente
comidas = [
    Pizza(),
    Hamburguesa(),
    Hotdog()
]

visitante_venta = VisitorVenta()

for comida in comidas:
    comida.accept(visitante_venta)
    print()