# Interfaz de Silla
class Silla:
    def descripcion(self):
        pass

# Implementación de Silla Moderna
class SillaModerna(Silla):
    def descripcion(self):
        return "Silla moderna"

# Implementación de Silla Victoriana
class SillaVictoriana(Silla):
    def descripcion(self):
        return "Silla victoriana"

# Implementación de Silla de Arte
class SillaArte(Silla):
    def descripcion(self):
        return "Silla de arte"

# Interfaz de Sofá
class Sofa:
    def descripcion(self):
        pass

# Implementación de Sofá Moderno
class SofaModerno(Sofa):
    def descripcion(self):
        return "Sofá moderno"

# Implementación de Sofá Victoriano
class SofaVictoriano(Sofa):
    def descripcion(self):
        return "Sofá victoriano"

# Implementación de Sofá de Arte
class SofaArte(Sofa):
    def descripcion(self):
        return "Sofá de arte"

# Interfaz de Mesa
class Mesa:
    def descripcion(self):
        pass

# Implementación de Mesa Moderna
class MesaModerna(Mesa):
    def descripcion(self):
        return "Mesa moderna"

# Implementación de Mesa Victoriana
class MesaVictoriana(Mesa):
    def descripcion(self):
        return "Mesa victoriana"

# Implementación de Mesa de Arte
class MesaArte(Mesa):
    def descripcion(self):
        return "Mesa de arte"

# Interfaz AbstractFactory
class AbstractFactory:
    def crear_silla(self):
        pass

    def crear_sofa(self):
        pass

    def crear_mesa(self):
        pass

# Implementación de la fábrica de muebles modernos
class ModernoFactory(AbstractFactory):
    def crear_silla(self):
        return SillaModerna()

    def crear_sofa(self):
        return SofaModerno()

    def crear_mesa(self):
        return MesaModerna()

# Implementación de la fábrica de muebles victorianos
class VictorianoFactory(AbstractFactory):
    def crear_silla(self):
        return SillaVictoriana()

    def crear_sofa(self):
        return SofaVictoriano()

    def crear_mesa(self):
        return MesaVictoriana()

# Implementación de la fábrica de muebles de arte
class ArteFactory(AbstractFactory):
    def crear_silla(self):
        return SillaArte()

    def crear_sofa(self):
        return SofaArte()

    def crear_mesa(self):
        return MesaArte()
    
# Crear una fábrica de muebles modernos
fabrica_moderna = ModernoFactory()

# Crear una silla moderna utilizando la fábrica de muebles modernos
silla_moderna = fabrica_moderna.crear_silla()
print(silla_moderna.descripcion())  # Output: Silla moderna

# Crear un sofá moderno utilizando la fábrica de muebles modernos
sofa_moderno = fabrica_moderna.crear_sofa()
print(sofa_moderno.descripcion())  # Output: Sofá moderno

# Crear una mesa moderna utilizando la fábrica de muebles modernos
mesa_moderna = fabrica_moderna.crear_mesa()
print(mesa_moderna.descripcion())  # Output: Mesa moderna

# Crear una fábrica de muebles victorianos
fabrica_victoriana = VictorianoFactory()

# Crear una silla victoriana utilizando la fábrica de muebles victorianos
silla_victoriana = fabrica_victoriana.crear_silla()
print(silla_victoriana.descripcion())  # Output: Silla victoriana

# Crear un sofá victoriano utilizando la fábrica de muebles victorianos
sofa_victoriano = fabrica_victoriana.crear_sofa()
print(sofa_victoriano.descripcion())  # Output: Sofá victoriano

# Crear una mesa victoriana utilizando la fábrica de muebles victorianos
mesa_victoriana = fabrica_victoriana.crear_mesa()
print(mesa_victoriana.descripcion())  # Output: Mesa victoriana

# Crear una fábrica de muebles de arte
fabrica_arte = ArteFactory()

# Crear una silla de arte utilizando la fábrica de muebles de arte
silla_arte = fabrica_arte.crear_silla()
print(silla_arte.descripcion())  # Output: Silla de arte

# Crear un sofá de arte utilizando la fábrica de muebles de arte
sofa_arte = fabrica_arte.crear_sofa()
print(sofa_arte.descripcion())  # Output: Sofá de arte

# Crear una mesa de arte utilizando la fábrica de muebles de arte
mesa_arte = fabrica_arte.crear_mesa()
print(mesa_arte.descripcion())  # Output: Mesa de arte