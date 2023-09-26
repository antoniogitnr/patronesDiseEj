from typing import Dict

class Jugador:
    def __init__(self, nombre: str, equipo: str, skin: str) -> None:
        self.nombre = nombre
        self.equipo = equipo
        self.skin = skin

    def mostrar_informacion(self) -> None:
        print(f"Jugador: {self.nombre}")
        print(f"Equipo: {self.equipo}")
        print(f"Skin: {self.skin}")
        print()

class FabricaJugadores:
    _jugadores: Dict[str, Jugador] = {}

    def obtener_jugador(self, nombre: str, equipo: str, skin: str) -> Jugador:
        if nombre not in self._jugadores:
            self._jugadores[nombre] = Jugador(nombre, equipo, skin)
        return self._jugadores[nombre]

def main():
    fabrica = FabricaJugadores()

    jugador1 = fabrica.obtener_jugador("Juan", "Equipo Rojo", "Skin A")
    jugador1.mostrar_informacion()

    jugador2 = fabrica.obtener_jugador("Pedro", "Equipo Azul", "Skin B")
    jugador2.mostrar_informacion()

    jugador3 = fabrica.obtener_jugador("Pablo", "Equipo Rojo", "Skin B")
    jugador3.mostrar_informacion()

if __name__ == "__main__":
    main()