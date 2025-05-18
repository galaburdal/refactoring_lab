import unittest
from run.order_manager import OrderManager
from run.commands.order import Order
from run.commands.place_order import PlaceOrderCommand

class TestIntegration(unittest.TestCase):
    def test_order_description_integration(self):
        order = Order("Latte with Milk and Syrup", 4.30)
        self.assertIn("Latte", order.description)
        self.assertGreater(order.cost, 4.00)

    def test_order_manager_stores_order(self):
        manager = OrderManager()
        order = Order("Espresso", 2.50)
        cmd = PlaceOrderCommand(manager, order)
        manager.execute_command(cmd)
        self.assertIn(order, manager._orders)
