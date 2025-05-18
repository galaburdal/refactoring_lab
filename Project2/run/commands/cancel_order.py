from .command import Command
from .order import Order

class CancelOrderCommand(Command):
    def __init__(self, manager, order: Order):
        self.manager = manager
        self.order = order

    def execute(self):
        self.manager.remove_order(self.order)

    def undo(self):
        self.manager.add_order(self.order)
