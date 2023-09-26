class Casa:
    def __init__(self):
        self.puertas = None
        self.ventanas = None
        self.techo = None

    def __str__(self):
        return f"Casa con {self.puertas} puertas, {self.ventanas} ventanas y un techo de {self.techo}"
        # Devuelve una representación en forma de cadena de la casa con la cantidad de puertas, ventanas y el tipo de techo.

class BuilderCasa:
    def construir_puertas(self):
        pass

    def construir_ventanas(self):
        pass

    def construir_techo(self):
        pass

    def obtener_casa(self):
        pass
        # Esta es una clase abstracta que define los métodos necesarios para construir una casa.
        # Los métodos son abstractos y deben ser implementados por las clases concretas.

class ConstructorCasaBasica(BuilderCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_puertas(self):
        self.casa.puertas = 2
        # Establece la cantidad de puertas de la casa en 2.

    def construir_ventanas(self):
        self.casa.ventanas = 4
        # Establece la cantidad de ventanas de la casa en 4.

    def construir_techo(self):
        self.casa.techo = "tejas"
        # Establece el tipo de techo de la casa como "tejas".

    def obtener_casa(self):
        return self.casa
        # Devuelve la casa construida.

class ConstructorCasaLujo(BuilderCasa):
    def __init__(self):
        self.casa = Casa()

    def construir_puertas(self):
        self.casa.puertas = 4
        # Establece la cantidad de puertas de la casa en 4.

    def construir_ventanas(self):
        self.casa.ventanas = 8
        # Establece la cantidad de ventanas de la casa en 8.

    def construir_techo(self):
        self.casa.techo = "mármol"
        # Establece el tipo de techo de la casa como "mármol".

    def obtener_casa(self):
        return self.casa
        # Devuelve la casa construida.
""" La clase  Director  en este ejemplo del patrón de diseño Builder se encarga de 
dirigir el proceso de construcción de la casa. Su función principal es coordinar y 
utilizar el builder seleccionado para construir la casa paso a paso.  """
class Director:
    def __init__(self):
        self.builder = None

    def construir_casa(self):
        self.builder.construir_puertas()
        self.builder.construir_ventanas()
        self.builder.construir_techo()
        # Utiliza el builder seleccionado para construir la casa paso a paso.

    def obtener_casa(self):
        return self.builder.obtener_casa()
        # Devuelve la casa construida.

# Ejemplo de uso
director = Director()

# Construcción de una casa básica
builder_basico = ConstructorCasaBasica()
director.builder = builder_basico

director.construir_casa()
casa_basica = director.obtener_casa()
print("Casa básica construida:")
print(casa_basica)

# Construcción de una casa de lujo
builder_lujo = ConstructorCasaLujo()
director.builder = builder_lujo

director.construir_casa()
casa_lujo = director.obtener_casa()
print("Casa de lujo construida:")
print(casa_lujo)