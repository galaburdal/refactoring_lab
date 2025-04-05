import unittest


class User:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        return f"User {self.name} registered successfully."

    def login(self):
        return f"User {self.name} logged in."


class Product:
    def __init__(self, product_id, name, description, price, quantity):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_details(self):
        return f"{self.name}: {self.description} - ${self.price} ({self.quantity} available)"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)

    def calculate_total(self):
        return sum(product.price for product in self.items)


class Order:
    def __init__(self, order_id, user, products):
        self.id = order_id
        self.user = user
        self.products = products
        self.total_price = sum(p.price for p in products)

    def create_order(self):
        return f"Order {self.id} created for user {self.user.name}. Total: ${self.total_price}"

    def cancel_order(self):
        return f"Order {self.id} cancelled."


class Payment:
    def __init__(self, order, amount):
        self.order = order
        self.amount = amount

    def pay(self):
        if self.amount >= self.order.total_price:
            return "Payment successful."
        return "Insufficient amount. Payment failed."

    def refund(self):
        return "Payment refunded."


# ----------- UNIT TESTS -----------

class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "Alice", "alice@example.com", "password123")
        self.product1 = Product(1, "Laptop", "Gaming laptop", 1200, 5)
        self.product2 = Product(2, "Mouse", "Wireless mouse", 50, 10)
        self.cart = Cart()

    def test_user_registration(self):
        self.assertEqual(self.user.register(), "User Alice registered successfully.")

    def test_user_login(self):
        self.assertEqual(self.user.login(), "User Alice logged in.")

    def test_add_product_to_cart(self):
        self.cart.add_product(self.product1)
        self.assertIn(self.product1, self.cart.items)

    def test_remove_product_from_cart(self):
        self.cart.add_product(self.product1)
        self.cart.remove_product(self.product1)
        self.assertNotIn(self.product1, self.cart.items)

    def test_calculate_cart_total(self):
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2)
        self.assertEqual(self.cart.calculate_total(), 1250)

    def test_create_order(self):
        order = Order(1, self.user, [self.product1, self.product2])
        self.assertEqual(order.create_order(), "Order 1 created for user Alice. Total: $1250")

    def test_cancel_order(self):
        order = Order(1, self.user, [self.product1])
        self.assertEqual(order.cancel_order(), "Order 1 cancelled.")

    def test_successful_payment(self):
        order = Order(1, self.user, [self.product1])
        payment = Payment(order, 1200)
        self.assertEqual(payment.pay(), "Payment successful.")

    def test_failed_payment(self):
        order = Order(1, self.user, [self.product1])
        payment = Payment(order, 1000)
        self.assertEqual(payment.pay(), "Insufficient amount. Payment failed.")

    def test_refund_payment(self):
        order = Order(1, self.user, [self.product1])
        payment = Payment(order, 1200)
        self.assertEqual(payment.refund(), "Payment refunded.")


if __name__ == "__main__":
    unittest.main()
