import unittest
from run.coffee.factory import CoffeeFactory

class TestCoffeeFactory(unittest.TestCase):
    def setUp(self):
        self.factory = CoffeeFactory()

    def test_create_espresso(self):
        coffee = self.factory.create_coffee("espresso")
        self.assertEqual(coffee.get_description(), "Espresso")
        self.assertAlmostEqual(coffee.get_cost(), 2.00)

    def test_create_latte(self):
        coffee = self.factory.create_coffee("latte")
        self.assertEqual(coffee.get_description(), "Latte")
        self.assertAlmostEqual(coffee.get_cost(), 3.50)

    def test_create_americano(self):
        coffee = self.factory.create_coffee("americano")
        self.assertEqual(coffee.get_description(), "Americano")
        self.assertAlmostEqual(coffee.get_cost(), 2.50)

    def test_create_cappuccino(self):
        coffee = self.factory.create_coffee("cappuccino")
        self.assertEqual(coffee.get_description(), "Cappuccino")
        self.assertAlmostEqual(coffee.get_cost(), 3.00)

    def test_invalid_type_raises_error(self):
        with self.assertRaises(ValueError):
            self.factory.create_coffee("unknown")

    def test_all_coffee_types_are_unique(self):
        espresso = self.factory.create_coffee("espresso")
        latte = self.factory.create_coffee("latte")
        self.assertNotEqual(espresso.get_description(), latte.get_description())

    def test_coffee_instance(self):
        coffee = self.factory.create_coffee("espresso")
        self.assertTrue(hasattr(coffee, "get_description"))
        self.assertTrue(hasattr(coffee, "get_cost"))
