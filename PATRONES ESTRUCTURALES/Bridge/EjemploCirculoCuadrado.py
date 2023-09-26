from abc import ABC, abstractmethod

# Clase de abstracción
class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def dibujar(self):
        pass

# Clase de implementación
class Color(ABC):
    @abstractmethod
    def pintar(self):
        pass

# Implementación concreta de color: Rojo
class Rojo(Color):
    def pintar(self):
        return "Rojo"

# Implementación concreta de color: Azul
class Azul(Color):
    def pintar(self):
        return "Azul"

# Clase de implementación concreta: Círculo
class Circulo(Figura):
    def __init__(self, color):
        super().__init__(color)

    def dibujar(self):
        return f"Círculo dibujado. Color: {self.color.pintar()}"

# Clase de implementación concreta: Cuadrado
class Cuadrado(Figura):
    def __init__(self, color):
        super().__init__(color)

    def dibujar(self):
        return f"Cuadrado dibujado. Color: {self.color.pintar()}"

# Cliente
if __name__ == "__main__":
    color_rojo = Rojo()
    color_azul = Azul()

    circulo_rojo = Circulo(color_rojo)
    circulo_azul = Circulo(color_azul)

    cuadrado_rojo = Cuadrado(color_rojo)
    cuadrado_azul = Cuadrado(color_azul)

    print(circulo_rojo.dibujar())
    print(circulo_azul.dibujar())
    print(cuadrado_rojo.dibujar())
    print(cuadrado_azul.dibujar())