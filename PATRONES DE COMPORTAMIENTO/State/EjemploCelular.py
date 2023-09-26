from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def press_button(self):
        pass

class HomeScreenState(State):
    def press_button(self):
        print("Mostrando pantalla de inicio")

class CallState(State):
    def press_button(self):
        print("Realizando una llamada")

class CameraState(State):
    def press_button(self):
        print("Abriendo la cámara")

class MusicState(State):
    def press_button(self):
        print("Reproduciendo música")

class CellPhone:
    def __init__(self):
        self.state = HomeScreenState()
    
    def press_button(self):
        self.state.press_button()
    
    def change_state(self, state):
        self.state = state

# Uso del patrón State para simular los botones de un celular
celular = CellPhone()

celular.press_button()

celular.change_state(CallState())
celular.press_button()

celular.change_state(CameraState())
celular.press_button()

celular.change_state(MusicState())
celular.press_button()