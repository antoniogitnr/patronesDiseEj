from abc import ABC, abstractmethod

class TarjetaCredito(ABC):
    @abstractmethod
    def realizar_pago(self, monto: float) -> bool:
        pass

class TarjetaCreditoReal(TarjetaCredito):
    def __init__(self, saldo: float):
        self._saldo = saldo

    def realizar_pago(self, monto: float) -> bool:
        if self._saldo >= monto:
            self._saldo -= monto
            print(f"Se ha realizado un pago de {monto} pesos.")
            return True
        else:
            print("Saldo insuficiente. No se puede realizar el pago.")
            return False

class TarjetaCreditoProxy(TarjetaCredito):
    def __init__(self, tarjeta_real: TarjetaCreditoReal):
        self._tarjeta_real = tarjeta_real

    def realizar_pago(self, monto: float) -> bool:
        if self.autenticar_usuario():
            return self._tarjeta_real.realizar_pago(monto)
        else:
            print("Autenticación fallida. No se puede realizar el pago.")
            return False

    def autenticar_usuario(self) -> bool:
        # Lógica para autenticar al usuario de la tarjeta
        return True

# Ejemplo de uso
tarjeta_real = TarjetaCreditoReal(5000.0)
tarjeta_proxy = TarjetaCreditoProxy(tarjeta_real)

tarjeta_proxy.realizar_pago(3000.0)
tarjeta_proxy.realizar_pago(4000.0)