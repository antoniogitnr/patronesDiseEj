class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Ejemplo de uso
s1 = Singleton()
s2 = Singleton()
s3 = Singleton()
print(s1 is s2 is s3)  # True, ambas variables contienen la misma instancia