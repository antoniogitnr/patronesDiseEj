class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Esta clase es un Singleton. ¡Solo puede haber una instancia!")
        else:
            Singleton._instance = self

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

# Ejemplo de uso
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
s3 = Singleton.get_instance()

print(s1 is s2 is s3)  # True, ambas variables contienen la misma instancia