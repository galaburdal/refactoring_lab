from refactored.interfaces import Printable, PriceCalculable

class Order(Printable, PriceCalculable):
    def __init__(self, client):
        self.client = client
        self._dishes = []

    def add_dish(self, dish):
        if not isinstance(dish, dict) or 'name' not in dish or 'price' not in dish:
            raise ValueError("Dish must be a dict with 'name' and 'price'")
        self._dishes.append(dish)

    def calculate_total(self):
        return sum(d['price'] for d in self._dishes)

    def print_invoice(self):
        print(f"Invoice for {self.client.name}")
        for dish in self._dishes:
            print(f"- {dish['name']}: {dish['price']}")
        print(f"Total: {self.calculate_total()}")
