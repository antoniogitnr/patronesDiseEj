class OrderSystem:
    def __init__(self):
        self._packaging_system = PackagingSystem()
        self._payment_system = PaymentSystem()
        self._delivery_system = DeliverySystem()

    def place_order(self, items: list):
        order_id = self._packaging_system.package_items(items)
        self._payment_system.process_payment(order_id)
        self._delivery_system.deliver_order(order_id)


class PackagingSystem:
    def package_items(self, items: list) -> str:
        order_id = self._generate_order_id()
        print(f"Empaquetando los siguientes artículos: {items}")
        print(f"Orden {order_id}: Artículos empaquetados correctamente.")
        return order_id

    def _generate_order_id(self) -> str:
        # Lógica para generar un ID de orden único
        pass


class PaymentSystem:
    def process_payment(self, order_id: str):
        print(f"Procesando pago para la orden {order_id}")
        print("Pago exitoso.")


class DeliverySystem:
    def deliver_order(self, order_id: str):
        print(f"Entregando orden {order_id}")
        print("Orden entregada correctamente.")


def make_phone_order(items: list):
    order_system = OrderSystem()
    order_system.place_order(items)


if __name__ == "__main__":
    items_to_order = ["Producto 1", "Producto 2", "Producto 3"]
    make_phone_order(items_to_order)