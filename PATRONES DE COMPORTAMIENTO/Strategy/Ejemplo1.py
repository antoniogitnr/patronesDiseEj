from abc import ABC, abstractmethod

# Interfaz de estrategia
class Estrategia(ABC):
    @abstractmethod
    def ejecutar_operacion(self, num1, num2):
        pass

# Estrategia concreta para la suma
class Suma(Estrategia):
    def ejecutar_operacion(self, num1, num2):
        return num1 + num2

# Estrategia concreta para la resta
class Resta(Estrategia):
    def ejecutar_operacion(self, num1, num2):
        return num1 - num2

# Estrategia concreta para la multiplicación
class Multiplicacion(Estrategia):
    def ejecutar_operacion(self, num1, num2):
        return num1 * num2

# Contexto
class Calculadora:
    def __init__(self, estrategia: Estrategia):
        self.estrategia = estrategia

    def cambiar_estrategia(self, estrategia: Estrategia):
        self.estrategia = estrategia

    def realizar_operacion(self, num1, num2):
        return self.estrategia.ejecutar_operacion(num1, num2)

# Ejemplo de uso
if __name__ == "__main__":
    suma = Suma()
    calculadora = Calculadora(suma)
    resultado = calculadora.realizar_operacion(5, 3)
    print("Resultado de la suma:", resultado)

    resta = Resta()
    calculadora.cambiar_estrategia(resta)
    resultado = calculadora.realizar_operacion(10, 7)
    print("Resultado de la resta:", resultado)

    multiplicacion = Multiplicacion()
    calculadora.cambiar_estrategia(multiplicacion)
    resultado = calculadora.realizar_operacion(4, 6)
    print("Resultado de la multiplicación:", resultado)