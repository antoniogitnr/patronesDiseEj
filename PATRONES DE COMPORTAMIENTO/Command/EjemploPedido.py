from abc import ABC, abstractmethod

# Interfaz Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        print('Command')

# Comandos concretos
class PedidoPastaCommand(Command):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        print('prepara pasta')
        self.chef.preparar_pasta()

class PedidoPizzaCommand(Command):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        print('prepara pizza')
        self.chef.preparar_pizza()

# Receptor
class Chef:
    def preparar_pasta(self):
        print("Chef: Preparando pasta a la carbonara sin cebolla")

    def preparar_pizza(self):
        print("Chef: Preparando pizza margarita")

# Invocador
class Mesero:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        print('Set mesero')
        self.command = command

    def enviar_pedido(self):
        print('Enviar pedido')
        self.command.execute()
        

# Uso del patrón Command
if __name__ == "__main__":
    chef = Chef()

    pedido_pasta_command = PedidoPastaCommand(chef)
    pedido_pizza_command = PedidoPizzaCommand(chef)

    mesero = Mesero()

    mesero.set_command(pedido_pasta_command)
    mesero.enviar_pedido()

    mesero.set_command(pedido_pizza_command)
    mesero.enviar_pedido()