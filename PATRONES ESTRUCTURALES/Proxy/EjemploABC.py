from abc import ABC, abstractmethod

class Subject(ABC):
    """
    La interfaz Subject declara operaciones comunes para RealSubject y Proxy.
    Mientras el cliente trabaje con RealSubject utilizando esta interfaz, podrás
    pasarle un proxy en lugar de un objeto real.
    """
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    """
    RealSubject contiene la lógica principal del negocio. Por lo general, los
    RealSubjects son capaces de realizar un trabajo útil que también puede ser
    muy lento o sensible, por ejemplo, corregir datos de entrada. Un Proxy
    puede resolver estos problemas sin realizar cambios en el código de
    RealSubject.
    """
    def request(self) -> None:
        print("RealSubject: Manejando la solicitud.")

class Proxy(Subject):
    """
    Proxy tiene una interfaz idéntica a la de RealSubject.
    """
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        Las aplicaciones más comunes del patrón Proxy son la carga perezosa,
        el almacenamiento en caché, el control de acceso, el registro, etc.
        Un Proxy puede realizar una de estas tareas y luego, dependiendo del
        resultado, pasar la ejecución al mismo método en un objeto RealSubject
        vinculado.
        """
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Verificando acceso antes de realizar una solicitud real.")
        return True

    def log_access(self) -> None:
        print("Proxy: Registrando la hora de la solicitud.", end="")

def client_code(subject: Subject) -> None:
    """
    Se supone que el código del cliente debe funcionar con todos los objetos
    (tanto sujetos como proxies) a través de la interfaz Subject para admitir
    tanto sujetos reales como proxies. Sin embargo, en la vida real, los
    clientes suelen trabajar directamente con sus sujetos reales. En este caso,
    para implementar el patrón de manera más sencilla, puedes extender tu proxy
    a partir de la clase del sujeto real.
    """
    # ...
    subject.request()
    # ...

if __name__ == "__main__":
    print("Cliente: Ejecutando el código del cliente con un sujeto real:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Cliente: Ejecutando el mismo código del cliente con un proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)