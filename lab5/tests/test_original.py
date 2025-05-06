import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from original.client import Client, Order

class TestOriginalOrder(unittest.TestCase):
    def setUp(self):
        self.client = Client("Alice", "123 Street")
        self.order = self.client.create_order()

    def test_add_single_dish(self):
        self.order.add_dish({'name': 'Pizza', 'price': 10})
        self.assertEqual(len(self.order.dishes), 1)

    def test_total_price_single_dish(self):
        self.order.add_dish({'name': 'Pizza', 'price': 10})
        self.assertEqual(self.order.calculate_total(), 10)

    def test_add_multiple_dishes(self):
        self.order.add_dish({'name': 'Soup', 'price': 6})
        self.order.add_dish({'name': 'Juice', 'price': 4})
        self.assertEqual(len(self.order.dishes), 2)

    def test_order_total_zero(self):
        self.assertEqual(self.order.calculate_total(), 0)

    def test_invoice_output(self):
        self.order.add_dish({'name': 'Pie', 'price': 7})
        try:
            self.order.print_invoice()
        except Exception as e:
            self.fail(f"print_invoice raised an exception: {e}")

    def test_client_str_representation(self):
        self.assertEqual(str(self.client), "Client: Alice, Address: 123 Street")

    def test_calculate_total_after_multiple_additions(self):
        self.order.add_dish({'name': 'Pasta', 'price': 10})
        self.order.add_dish({'name': 'Cake', 'price': 5})
        self.order.add_dish({'name': 'Water', 'price': 2})
        self.assertEqual(self.order.calculate_total(), 17)

    def test_order_object_is_instance_of_order(self):
        self.assertIsInstance(self.order, Order)

    def test_empty_dishes_list(self):
        self.assertEqual(self.order.dishes, [])

    def test_add_dish_with_zero_price(self):
        self.order.add_dish({'name': 'Ice', 'price': 0})
        self.assertEqual(self.order.calculate_total(), 0)

