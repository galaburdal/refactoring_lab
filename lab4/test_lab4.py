import unittest
from models.menu import Menu
from models.dish import Dish
from models.client import Client
from patterns.order_factory import StandardOrderFactory
from patterns.order_database_singleton import OrderDatabase
from patterns.observer import OrderObserver
from models.kitchen_notifier import KitchenNotifier

class TestLab4(unittest.TestCase):
    def test_add_dish_to_menu(self):
        menu = Menu()
        dish = Dish("Піца", 150)
        menu.add_dish(dish)
        self.assertIn(dish, menu.get_dishes())

    def test_create_client(self):
        client = Client("Liza")
        self.assertEqual(client.name, "Liza")

    def test_order_total(self):
        client = Client("Test")
        factory = StandardOrderFactory()
        order = factory.create_order(client)
        order.add_dish(Dish("Паста", 100))
        order.add_dish(Dish("Суп", 80))
        self.assertEqual(order.get_total(), 180)

    def test_attach_observer(self):
        obs = OrderObserver()
        kitchen = KitchenNotifier()
        obs.attach(kitchen)
        self.assertIn(kitchen, obs._observers)

    def test_order_database_singleton(self):
        db1 = OrderDatabase()
        db2 = OrderDatabase()
        self.assertIs(db1, db2)

    def test_add_order_to_database(self):
        db = OrderDatabase()
        db._orders.clear()
        client = Client("Test")
        order = StandardOrderFactory().create_order(client)
        db.add_order(order)
        self.assertIn(order, db.get_all_orders())

    def test_create_order_via_factory(self):
        client = Client("Liza")
        factory = StandardOrderFactory()
        order = factory.create_order(client)
        self.assertEqual(order.client, client)

    def test_add_order_to_client(self):
        client = Client("Liza")
        order = StandardOrderFactory().create_order(client)
        client.add_order(order)
        self.assertIn(order, client.get_orders())

    def test_empty_menu(self):
        menu = Menu()
        self.assertEqual(len(menu.get_dishes()), 0)

    def test_dish_creation(self):
        dish = Dish("Борщ", 60.0)
        self.assertEqual(dish.name, "Борщ")
        self.assertEqual(dish.price, 60.0)

if __name__ == "__main__":
    unittest.main()
