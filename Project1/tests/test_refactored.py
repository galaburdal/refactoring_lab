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
        self.dish3 = Dish("Salad", 70.0)

    def test_client_name(self):
        self.assertEqual(self.client.name, "Test User")

    def test_add_order_to_client(self):
        self.client.add_order(self.order)
        self.assertIn(self.order, self.client.get_orders())

    def test_get_orders_empty(self):
        new_client = Client("No Orders")
        self.assertEqual(new_client.get_orders(), [])

    def test_add_multiple_orders_to_client(self):
        order2 = Order(self.client)
        self.client.add_order(self.order)
        self.client.add_order(order2)
        self.assertEqual(len(self.client.get_orders()), 2)

    def test_add_dish_to_order(self):
        self.order.add_dish(self.dish1)
        self.assertIn(self.dish1, self.order._dishes)

    def test_remove_dish(self):
        self.order.add_dish(self.dish1)
        self.order.remove_dish(self.dish1)
        self.assertNotIn(self.dish1, self.order._dishes)

    def test_remove_nonexistent_dish(self):
        try:
            self.order.remove_dish(self.dish1)
            self.assertTrue(True)
        except Exception:
            self.fail("remove_dish() raised Exception unexpectedly!")

    def test_calculate_total(self):
        self.order.add_dish(self.dish1)
        self.order.add_dish(self.dish2)
        self.assertEqual(self.order.calculate_total(), 150.75)

    def test_calculate_empty_order_total(self):
        self.assertEqual(self.order.calculate_total(), 0)

    def test_add_same_dish_multiple_times(self):
        self.order.add_dish(self.dish1)
        self.order.add_dish(self.dish1)
        self.assertEqual(len(self.order._dishes), 1)

    def test_order_client_association(self):
        self.assertEqual(self.order.client, self.client)

    def test_dish_price(self):
        self.assertEqual(self.dish1.price, 100.5)

    def test_dish_name(self):
        self.assertEqual(self.dish2.name, "Soup")

    def test_order_dishes_initially_empty(self):
        self.assertEqual(self.order._dishes, [])

    def test_add_three_dishes(self):
        self.order.add_dish(self.dish1)
        self.order.add_dish(self.dish2)
        self.order.add_dish(self.dish3)
        self.assertEqual(len(self.order._dishes), 3)

    def test_order_total_with_three_dishes(self):
        self.order.add_dish(self.dish1)
        self.order.add_dish(self.dish2)
        self.order.add_dish(self.dish3)
        self.assertAlmostEqual(self.order.calculate_total(), 220.75)

    def test_order_instance_type(self):
        self.assertIsInstance(self.order, Order)

    def test_client_instance_type(self):
        self.assertIsInstance(self.client, Client)

    def test_dish_instance_type(self):
        self.assertIsInstance(self.dish1, Dish)

    def test_get_orders_returns_list(self):
        self.assertIsInstance(self.client.get_orders(), list)

if __name__ == '__main__':
    unittest.main()
