import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from refactored.client import Client
from refactored.order import Order

class TestRefactoredOrder(unittest.TestCase):
    def setUp(self):
        self.client = Client("Bob", "456 Avenue")
        self.order = Order(self.client)

    def test_add_valid_dish(self):
        self.order.add_dish({'name': 'Burger', 'price': 8})
        self.assertEqual(len(self.order._dishes), 1)

    def test_total_price(self):
        self.order.add_dish({'name': 'Burger', 'price': 8})
        self.order.add_dish({'name': 'Fries', 'price': 4})
        self.assertEqual(self.order.calculate_total(), 12)

    def test_invoice_output(self):
        self.order.add_dish({'name': 'Burger', 'price': 8})
        try:
            self.order.print_invoice()
        except Exception as e:
            self.fail(f"print_invoice failed: {e}")

    def test_reject_invalid_dish_type(self):
        with self.assertRaises(ValueError):
            self.order.add_dish("not a dish")

    def test_calculate_total_empty(self):
        self.assertEqual(self.order.calculate_total(), 0)

    def test_client_str_representation(self):
        self.assertEqual(str(self.client), "Client: Bob, Address: 456 Avenue")

    def test_add_multiple_dishes_and_total(self):
        self.order.add_dish({'name': 'Steak', 'price': 15})
        self.order.add_dish({'name': 'Salad', 'price': 5})
        self.assertEqual(self.order.calculate_total(), 20)

    def test_empty_dishes_list_initially(self):
        self.assertEqual(self.order._dishes, [])

    def test_invalid_dish_missing_name(self):
        with self.assertRaises(ValueError):
            self.order.add_dish({'price': 12})

    def test_invalid_dish_missing_price(self):
        with self.assertRaises(ValueError):
            self.order.add_dish({'name': 'Soda'})

