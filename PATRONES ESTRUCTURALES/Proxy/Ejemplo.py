from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Manejando la solicitud.")

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy: Verificando acceso antes de realizar una solicitud real.")
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print(' Lógica para verificar el acceso')
        return True

    def log_access(self):
        print('Lógica para registrar el acceso')
        

# Ejemplo de uso
real_subject = RealSubject()
proxy = Proxy(real_subject)

# Llamada a través del proxy
proxy.request()