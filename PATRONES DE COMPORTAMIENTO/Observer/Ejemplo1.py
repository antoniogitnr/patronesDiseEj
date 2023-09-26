from abc import ABC, abstractmethod

# Interfaz del Sujeto
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Interfaz del Observador
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Observador Concreto
class ConcreteObserver(Observer):
    def update(self, message):
        print("Mensaje recibido:", message)

# Cliente
if __name__ == "__main__":
    # Crear sujeto
    subject = Subject()

    # Crear observadores
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    # Adjuntar observadores al sujeto
    subject.attach(observer1)
    subject.attach(observer2)

    # Notificar a los observadores
    subject.notify("¡Hola, observadores!")

    # Desvincular un observador
    subject.detach(observer2)

    # Notificar nuevamente a los observadores
    subject.notify("¡Adiós, observadores!")