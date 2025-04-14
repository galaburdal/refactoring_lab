import unittest
from refactored_code.client import Client
from refactored_code.order import Order

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TestClientOrder(unittest.TestCase):
    def setUp(self):
        self.client = Client("Test User")
        self.order = Order(self.client)
        self.dish1 = Dish("Pizza", 100.5)
        self.dish2 = Dish("Soup", 50.25)

    def test_client_name(self):
        self.assertEqual(self.client.name, "Test User")

    def test_add_order_to_client(self):
        self.client.add_order(self.order)
        self.assertIn(self.order, self.client.get_orders())

    def test_add_dish_to_order(self):
        self.order.add_dish(self.dish1)
        self.assertIn(self.dish1, self.order._dishes)

    def test_remove_dish(self):
        self.order.add_dish(self.dish1)
        self.order.remove_dish(self.dish1)
        self.assertNotIn(self.dish1, self.order._dishes)

    def test_calculate_total(self):
        self.order.add_dish(self.dish1)
        self.order.add_dish(self.dish2)
        self.assertEqual(self.order.calculate_total(), 150.75)

if __name__ == '__main__':
    unittest.main()