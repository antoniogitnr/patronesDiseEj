class Target:
    """
    El Target define la interfaz específica del dominio utilizada por el código del cliente.
    """
    def request(self) -> str:
        return "Target: Comportamiento predeterminado del target."


class Adaptee:
    """
    El Adaptee contiene un comportamiento útil, pero su interfaz es incompatible
    con el código del cliente existente. El Adaptee necesita alguna adaptación antes de que
    el código del cliente pueda usarlo.
    """
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    El Adapter hace que la interfaz del Adaptee sea compatible con la interfaz del Target
    a través de la herencia múltiple.
    """
    def request(self) -> str:
        return f"Adapter: (TRADUCIDO) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    El código del cliente admite todas las clases que siguen la interfaz del Target.
    """
    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: Puedo trabajar perfectamente con objetos Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: La clase Adaptee tiene una interfaz extraña. "
          "Mira, no la entiendo:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con ella a través del Adapter:")
    adapter = Adapter()
    client_code(adapter)