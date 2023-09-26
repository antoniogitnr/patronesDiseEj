class Producto:
    def __init__(self):
        self.parte_a = None
        self.parte_b = None

    def set_parte_a(self, parte_a):
        self.parte_a = parte_a

    def set_parte_b(self, parte_b):
        self.parte_b = parte_b

    def __str__(self):
        return f"Parte A: {self.parte_a}, Parte B: {self.parte_b}"


class Builder:
    def construir_parte_a(self):
        pass

    def construir_parte_b(self):
        pass

    def obtener_resultado(self):
        pass


class ConstructorConcreto(Builder):
    def __init__(self):
        self.producto = Producto()

    def construir_parte_a(self):
        self.producto.set_parte_a("Parte A construida")

    def construir_parte_b(self):
        self.producto.set_parte_b("Parte B construida")

    def obtener_resultado(self):
        return self.producto


# Ejemplo de uso
constructor = ConstructorConcreto()
constructor.construir_parte_a()
constructor.construir_parte_b()
producto = constructor.obtener_resultado()
print(producto)