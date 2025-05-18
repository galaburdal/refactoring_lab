class OrderManager:
    """Контекст для управління замовленнями"""
    def __init__(self):
        self._orders = []
        self._history = []

    def add_order(self, order):
        self._orders.append(order)
        print(f"✔ Added: {order}")

    def remove_order(self, order):
        if order in self._orders:
            self._orders.remove(order)
            print(f"✖ Removed: {order}")

    def execute_command(self, command):
        command.execute()
        self._history.append(command)

    def undo_last(self):
        if self._history:
            last_command = self._history.pop()
            last_command.undo()

    def list_orders(self):
        print("📋 Current Orders:")
        for o in self._orders:
            print(f"  - {o}")
