import copy

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None
    
    def set_parent(self, parent):
        self.parent = parent

class SomeComponent:
    """
    Python proporciona su propia interfaz de prototipo a través de las funciones
    `copy.copy` y `copy.deepcopy`. Y cualquier clase que desee implementar
    implementaciones personalizadas debe sobrescribir las funciones miembro
    `__copy__` y `__deepcopy__`.
    """
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref
    
    def __copy__(self):
        """
        Crea una copia superficial. Este método se llamará cada vez que alguien
        llame a `copy.copy` con este objeto y el valor devuelto se utilizará como
        la nueva copia superficial.
        """
        # Primero, creemos copias de los objetos anidados.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)
        
        # Luego, clonemos el objeto en sí, utilizando las copias preparadas de los
        # objetos anidados.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)
        return new
    
    def __deepcopy__(self, memo=None):
        """
        Crea una copia profunda. Este método se llamará cada vez que alguien
        llame a `copy.deepcopy` con este objeto y el valor devuelto se utilizará
        como la nueva copia profunda.
        ¿Cuál es el uso del argumento `memo`? Memo es el diccionario que utiliza
        la biblioteca `deepcopy` para evitar copias recursivas infinitas en
        instancias de referencias circulares. Pásalo a todas las llamadas a
        `deepcopy` que hagas en la implementación de `__deepcopy__` para evitar
        recursiones infinitas.
        """
        if memo is None:
            memo = {}
        
        # Primero, creemos copias de los objetos anidados.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
        
        # Luego, clonemos el objeto en sí, utilizando las copias preparadas de los
        # objetos anidados.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new

if __name__ == "__main__":
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)
    
    shallow_copied_component = copy.copy(component)
    # Cambiemos la lista en shallow_copied_component y veamos si cambia en component.
    shallow_copied_component.some_list_of_objects.append("another object")
    
    if component.some_list_of_objects[-1] == "another object":
        print(
            "Añadir elementos a some_list_of_objects de `shallow_copied_component` "
            "lo añade también a some_list_of_objects de `component`."
        )
    else:
        print(
            "Añadir elementos a some_list_of_objects de `shallow_copied_component` "
            "no lo añade a some_list_of_objects de `component`."
        )
    
    # Cambiemos el conjunto en la lista de objetos.
    component.some_list_of_objects[1].add(4)
    
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Cambiar objetos en some_list_of_objects de `component` "
            "cambia ese objeto en some_list_of_objects de `shallow_copied_component`."
        )
    else:
        print(
            "Cambiar objetos en some_list_of_objects de `component` "
            "no cambia ese objeto en some_list_of_objects de `shallow_copied_component`."
        )
    
    deep_copied_component = copy.deepcopy(component)
    
    # Cambiemos la lista en deep_copied_component y veamos si cambia en component.
    deep_copied_component.some_list_of_objects.append("one more object")
    
    if component.some_list_of_objects[-1] == "one more object":
        print(
            "Añadir elementos a some_list_of_objects de `deep_copied_component` "
            "lo añade también a some_list_of_objects de `component`."
        )
    else:
        print(
            "Añadir elementos a some_list_of_objects de `deep_copied_component` "
            "no lo añade a some_list_of_objects de `component`."
        )
    
    # Cambiemos el conjunto en la lista de objetos.
    component.some_list_of_objects[1].add(10)
    
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Cambiar objetos en some_list_of_objects de `component` "
            "cambia ese objeto en some_list_of_objects de `deep_copied_component`."
        )
    else:
        print(
            "Cambiar objetos en some_list_of_objects de `component` "
            "no cambia ese objeto en some_list_of_objects de `deep_copied_component`."
        )
    
    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    
    print(
        "^^ Esto muestra que los objetos copiados en profundidad contienen la misma referencia, no se clonan repetidamente."
    )