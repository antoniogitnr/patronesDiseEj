import copy

class Prototype:
    def __init__(self):
        self.name = "Prototipo"
    
    def clone(self):
        
        print('--------------- Crea una copia profunda del objeto actual utilizando la función deepcopy.')
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self):
        super().__init__()
        self.attribute = "Atributo predeterminado"
        print('------------------desde el constructor ConcretePrototype')
    
    def set_attribute(self, attribute):
       
        print(' --------------------Establece el valor del atributo.')
        self.attribute = attribute
    
    def display(self):
        
        print('----------------------Muestra el nombre y el atributo del prototipo.')
        print(f"Nombre: {self.name}")
        print(f"Atributo: {self.attribute}")

if __name__ == "__main__":
    print('-----------------Crear una instancia del prototipo y mostrarla')
    prototipo = ConcretePrototype()
    prototipo.display()
    
    print('----------------Clonar el prototipo')
    prototipo_clonado = prototipo.clone()
    prototipo_clonado.display()
    
    print('-----------Cambiar el atributo del clon')
    prototipo_clonado.set_attribute("Atributo modificado")
    prototipo_clonado.display()