from abc import ABC, abstractmethod

# Interfaz del Sujeto
class YouTuber:
    def __init__(self):
        self._subscribers = []

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, video):
        for subscriber in self._subscribers:
            subscriber.update(video)

# Interfaz del Observador
class Subscriber(ABC):
    @abstractmethod
    def update(self, video):
        pass

# Observador Concreto
class ConcreteSubscriber(Subscriber):
    def __init__(self, name):
        self._name = name

    def update(self, video):
        print(f"{self._name} ha recibido una notificación del nuevo video: {video}")

# Cliente
if __name__ == "__main__":
    # Crear YouTuber
    youtuber = YouTuber()

    # Crear suscriptores
    subscriber1 = ConcreteSubscriber("Suscriptor 1")
    subscriber2 = ConcreteSubscriber("Suscriptor 2")
    subscriber3 = ConcreteSubscriber("Suscriptor 3")
    subscriber4 = ConcreteSubscriber("Suscriptor 4")
    subscriber5 = ConcreteSubscriber("Suscriptor 5")

    # Adjuntar suscriptores al YouTuber
    youtuber.attach(subscriber1)
    youtuber.attach(subscriber2)
    youtuber.attach(subscriber3)
    youtuber.attach(subscriber4)
    youtuber.attach(subscriber5)

    # Publicar videos y notificar a los suscriptores
    videos = ["Video 1", "Video 2", "Video 3"]
    for video in videos:
        youtuber.notify(video)