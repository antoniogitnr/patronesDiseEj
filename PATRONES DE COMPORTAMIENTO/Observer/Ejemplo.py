from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    """
    La interfaz Subject declara un conjunto de métodos para gestionar suscriptores.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Adjunta un observador al sujeto.
        """
        pass
    
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Desvincula un observador del sujeto.
        """
        pass
    
    @abstractmethod
    def notify(self) -> None:
        """
        Notifica a todos los observadores sobre un evento.
        """
        pass

class ConcreteSubject(Subject):
    """
    El ConcreteSubject posee un estado importante y notifica a los observadores cuando el estado cambia.
    """
    _state: int = None
    """
    Por simplicidad, el estado del ConcreteSubject, esencial para todos los suscriptores, se almacena en esta variable.
    """
    _observers: List[Observer] = []
    """
    Lista de suscriptores. En la vida real, la lista de suscriptores puede almacenarse de manera más completa (categorizada por tipo de evento, etc.).
    """
    def attach(self, observer: Observer) -> None:
        print("Sujeto: Se adjuntó un observador.")
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    """
    Métodos de gestión de suscripción.
    """
    def notify(self) -> None:
        """
        Desencadena una actualización en cada suscriptor.
        """
        print("Sujeto: Notificando a los observadores...")
        for observer in self._observers:
            observer.update(self)
    
    def some_business_logic(self) -> None:
        """
        Por lo general, la lógica de suscripción es solo una fracción de lo que realmente puede hacer un sujeto.
        Los sujetos suelen tener alguna lógica empresarial importante, que desencadena un método de notificación cada vez que algo importante está a punto de suceder (o después).
        """
        print("\nSujeto: Estoy haciendo algo importante.")
        self._state = randrange(0, 10)
        print(f"Sujeto: Mi estado acaba de cambiar a: {self._state}")
        self.notify()

class Observer(ABC):
    """
    La interfaz Observer declara el método de actualización, utilizado por los sujetos.
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recibe una actualización del sujeto.
        """
        pass

"""
Los Observadores Concretos reaccionan a las actualizaciones emitidas por el Sujeto al que se habían adjuntado.
"""
class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ObservadorConcretoA: Reaccionó al evento")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ObservadorConcretoB: Reaccionó al evento")

if __name__ == "__main__":
    # Código del cliente.
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)
    subject.some_business_logic()
    subject.some_business_logic()
    subject.detach(observer_a)
    subject.some_business_logic()