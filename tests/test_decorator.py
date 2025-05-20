import unittest
from run.coffee.factory import CoffeeFactory
from run.decorators.decorators import Milk, Syrup, WhippedCream

class TestDecorators(unittest.TestCase):
    def setUp(self):
        self.factory = CoffeeFactory()
        self.base = self.factory.create_coffee("espresso")  # базова ціна: 2.00

    def test_add_milk(self):
        coffee = Milk(self.base)  # 2.00 + 0.30
        self.assertIn("Milk", coffee.get_description())
        self.assertAlmostEqual(coffee.get_cost(), 2.50)

    def test_add_syrup(self):
        coffee = Syrup(self.base)  # 2.00 + 0.50
        self.assertIn("Syrup", coffee.get_description())
        self.assertAlmostEqual(coffee.get_cost(), 2.30)

    def test_add_whipped_cream(self):
        coffee = WhippedCream(self.base)  # 2.00 + 0.70
        self.assertIn("Whipped Cream", coffee.get_description())
        self.assertAlmostEqual(coffee.get_cost(), 2.70)

    def test_multiple_ingredients(self):
        coffee = WhippedCream(Milk(Syrup(self.base)))  # 2.00 + 0.50 + 0.30 + 0.70
        self.assertIn("Milk", coffee.get_description())
        self.assertIn("Syrup", coffee.get_description())
        self.assertIn("Whipped Cream", coffee.get_description())
        self.assertAlmostEqual(coffee.get_cost(), 2.00 + 0.50 + 0.30 + 0.70)

    def test_chaining_preserves_methods(self):
        coffee = Milk(self.base)
        self.assertTrue(hasattr(coffee, "get_description"))
        self.assertTrue(hasattr(coffee, "get_cost"))
