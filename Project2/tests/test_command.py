import unittest
from run.order_manager import OrderManager
from run.commands.order import Order
from run.commands.place_order import PlaceOrderCommand
from run.commands.cancel_order import CancelOrderCommand

class TestCommandPattern(unittest.TestCase):
    def setUp(self):
        self.manager = OrderManager()
        self.order = Order("Test Coffee", 5.00)
        self.place = PlaceOrderCommand(self.manager, self.order)
        self.cancel = CancelOrderCommand(self.manager, self.order)

    def test_place_order_executes(self):
        self.manager.execute_command(self.place)
        self.assertEqual(len(self.manager._orders), 1)

    def test_cancel_order_executes(self):
        self.manager.execute_command(self.place)
        self.manager.execute_command(self.cancel)
        self.assertEqual(len(self.manager._orders), 0)

    def test_undo_works_for_place(self):
        self.manager.execute_command(self.place)
        self.manager.undo_last()
        self.assertEqual(len(self.manager._orders), 0)

    def test_undo_works_for_cancel(self):
        self.manager.execute_command(self.place)
        self.manager.execute_command(self.cancel)
        self.manager.undo_last()
        self.assertEqual(len(self.manager._orders), 1)

    def test_multiple_commands_history(self):
        self.manager.execute_command(self.place)
        self.manager.execute_command(self.cancel)
        self.assertEqual(len(self.manager._history), 2)

    def test_undo_empty_history_safe(self):
        try:
            self.manager.undo_last()
        except Exception as e:
            self.fail(f"Undo raised unexpected error: {e}")
