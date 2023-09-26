class SingletonMeta(type):
    """
    La clase Singleton puede implementarse de diferentes formas en Python. Algunos
    métodos posibles incluyen: clase base, decorador, metaclase. Usaremos la
    metaclase porque es la más adecuada para este propósito.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Los posibles cambios en el valor del argumento `__init__` no afectan
        a la instancia devuelta.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finalmente, cualquier singleton debería definir alguna lógica de negocio, que puede ser
        ejecutada en su instancia.
        """
        # ...


if __name__ == "__main__":
    # Código del cliente.
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print("El Singleton funciona, ambas variables contienen la misma instancia.")
    else:
        print("El Singleton falló, las variables contienen instancias diferentes.")