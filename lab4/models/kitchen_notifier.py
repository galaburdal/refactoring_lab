from models.interfaces import INotifier

class KitchenNotifier(INotifier):
    def notify(self, order):
        print(f"[Кухня] Нове замовлення від {order.client.name}, страв: {len(order._dishes)}")
