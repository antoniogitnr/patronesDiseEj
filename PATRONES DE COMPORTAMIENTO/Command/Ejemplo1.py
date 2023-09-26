from abc import ABC, abstractmethod

# Interfaz Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Comando concreto
class SimpleCommand(Command):
    def execute(self):
        print("Comando simple ejecutado")

# Comando complejo
class ComplexCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.do_something()
        self.receiver.do_something_else()

# Receptor
class Receiver:
    def do_something(self):
        print("Haciendo algo...")

    def do_something_else(self):
        print("Haciendo algo más...")

# Invocador
class Invoker:
    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()

# Uso del patrón Command
if __name__ == "__main__":
    receiver = Receiver()

    simple_command = SimpleCommand()
    complex_command = ComplexCommand(receiver)

    invoker = Invoker()
    invoker.set_command(simple_command)
    invoker.execute_command()

    invoker.set_command(complex_command)
    invoker.execute_command()