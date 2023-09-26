class Producto:
    def transportar(self):
        pass

class ProductoTerrestre(Producto):
    def transportar(self):
        print("Transportando por tierra")

class ProductoMaritimo(Producto):
    def transportar(self):
        print("Transportando por mar")

class Creador:
    def factory_method(self):
        pass

    def transportar_producto(self):
        producto = self.factory_method()
        producto.transportar()

class CreadorTerrestre(Creador):
    def factory_method(self):
        return ProductoTerrestre()

class CreadorMaritimo(Creador):
    def factory_method(self):
        return ProductoMaritimo()
    
creador_terrestre = CreadorTerrestre()
creador_terrestre.transportar_producto()  # Transportando por tierra

creador_maritimo = CreadorMaritimo()
creador_maritimo.transportar_producto()  # Transportando por mar