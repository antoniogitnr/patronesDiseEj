# La clase Target define la interfaz específica del dominio utilizada por el cliente
class Target:
    def request(self) -> str:
        return "Target: Comportamiento predeterminado del target."


# La clase Adaptee contiene un comportamiento útil pero con una interfaz incompatible
class Adaptee:
    def specific_request(self) -> str:
        return "Comportamiento específico del Adaptee."


# La clase Adapter adapta la interfaz del Adaptee a la interfaz del Target
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (Adaptado) {self.adaptee.specific_request()}"


# Función cliente que utiliza el Target
def client_code(target: Target) -> None:
    print(target.request())


# Ejemplo de uso del patrón Adapter
if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print("Cliente: Puedo trabajar con el Target:")
    target = Target()
    client_code(target)

    print("\nCliente: Pero también puedo trabajar con el Adaptee a través del Adapter:")
    client_code(adapter)