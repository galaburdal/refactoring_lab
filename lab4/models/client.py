class Client:
    def __init__(self, name: str):
        self.name = name
        self._orders = []

    def add_order(self, order):
        '''Додає замовлення клієнту'''
        self._orders.append(order)

    def get_orders(self):
        '''Отримує список замовлень'''
        return self._orders
