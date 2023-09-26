""" Paso 1: Define una clase base para tu producto."""
class Producto:
    def operacion(self):
        pass
""" Paso 2: Crea las clases concretas que implementen la clase base. """
class ProductoConcreto1(Producto):
    def operacion(self):
        print('2.1.Implementa la operación específica para ProductoConcreto1')
        # Implementa la operación específica para ProductoConcreto1
        

class ProductoConcreto2(Producto):
    def operacion(self):
        print('2.2.Implementa la operación específica para ProductoConcreto2')
        # Implementa la operación específica para ProductoConcreto2
        
""" Paso 3: Crea la clase creadora (Creator) que contiene el método Factory Method. """
class Creador:
    def factory_method(self):
        pass

    def operacion(self):
        producto = self.factory_method()
        print('1.Realiza operaciones con el producto')
        # Realiza operaciones con el producto
        producto.operacion()
""" Paso 4: Implementa las clases creadoras concretas que hereden de la clase creadora y sobrescriban el método factory_method. """
class CreadorConcreto1(Creador):
    def factory_method(self):
        return ProductoConcreto1()

class CreadorConcreto2(Creador):
    def factory_method(self):
        return ProductoConcreto2()
""" Paso 5: Utiliza el Factory Method para crear objetos. """
print("\n")
creador = CreadorConcreto1()
creador.operacion()  # Crea y utiliza un ProductoConcreto1
print("\n")
creador = CreadorConcreto2()
creador.operacion()  # Crea y utiliza un ProductoConcreto2
print("\n")
