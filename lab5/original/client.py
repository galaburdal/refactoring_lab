class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.orders = []

    def create_order(self):
        return Order(self)

    def __str__(self):
        return f"Client: {self.name}, Address: {self.address}"

class Order:
    def __init__(self, client):
        self.client = client
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def calculate_total(self):
        return sum(dish['price'] for dish in self.dishes)

    def print_invoice(self):
        print(f"Invoice for {self.client.name}")
        for dish in self.dishes:
            print(f"- {dish['name']}: {dish['price']}")
        print(f"Total: {self.calculate_total()}")
