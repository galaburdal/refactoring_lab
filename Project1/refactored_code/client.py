class Client:
    def __init__(self, name):
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def add_order(self, order):
        self._orders.append(order)

    def get_orders(self):
        return self._orders[:]