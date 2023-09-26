# Interfaz ProductoA
class ProductoA:
    def descripcion(self):
        pass

# Interfaz ProductoB
class ProductoB:
    def descripcion(self):
        pass

# Implementación de ProductoA1
class ProductoA1(ProductoA):
    def descripcion(self):
        return "Producto A1"

# Implementación de ProductoA2
class ProductoA2(ProductoA):
    def descripcion(self):
        return "Producto A2"

# Implementación de ProductoB1
class ProductoB1(ProductoB):
    def descripcion(self):
        return "Producto B1"

# Implementación de ProductoB2
class ProductoB2(ProductoB):
    def descripcion(self):
        return "Producto B2"

# Interfaz AbstractFactory
class AbstractFactory:
    def crear_producto_a(self):
        pass

    def crear_producto_b(self):
        pass

# Implementación de la fábrica FactoryA
class FactoryA(AbstractFactory):
    def crear_producto_a(self):
        return ProductoA1()

    def crear_producto_b(self):
        return ProductoB1()

# Implementación de la fábrica FactoryB
class FactoryB(AbstractFactory):
    def crear_producto_a(self):
        return ProductoA2()

    def crear_producto_b(self):
        return ProductoB2()