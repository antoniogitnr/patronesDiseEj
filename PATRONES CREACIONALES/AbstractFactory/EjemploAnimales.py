# Interfaz Animal
class Animal:
    def hacer_sonido(self):
        pass

# Implementación de Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau!"

# Implementación de Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau!"

# Interfaz AbstractFactory
class AbstractFactory:
    def crear_animal(self):
        pass

# Implementación de la fábrica de Perros
class PerroFactory(AbstractFactory):
    def crear_animal(self):
        return Perro()

# Implementación de la fábrica de Gatos
class GatoFactory(AbstractFactory):
    def crear_animal(self):
        return Gato()
    
    
# Crear una fábrica de Perros
fabrica_perros = PerroFactory()

# Crear un Perro utilizando la fábrica de Perros
perro = fabrica_perros.crear_animal()
print(perro.hacer_sonido())  # Output: Guau guau!

# Crear una fábrica de Gatos
fabrica_gatos = GatoFactory()

# Crear un Gato utilizando la fábrica de Gatos
gato = fabrica_gatos.crear_animal()
print(gato.hacer_sonido())  # Output: Miau miau!