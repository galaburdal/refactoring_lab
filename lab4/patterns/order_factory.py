from models.order import Order
from models.interfaces import IOrderFactory


class StandardOrderFactory(IOrderFactory):
    def create_order(self, client):
        return Order(client)
