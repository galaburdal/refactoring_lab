class Order:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})
        self.total += price * quantity

    def print_invoice(self):
        print("===== INVOICE =====")
        for item in self.items:
            print(f"{item['name']} x {item['quantity']} = {item['price'] * item['quantity']}$")
        print(f"Total: {self.total}$")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write("===== INVOICE =====\n")
            for item in self.items:
                f.write(f"{item['name']} x {item['quantity']} = {item['price'] * item['quantity']}$\n")
            f.write(f"Total: {self.total}$\n")
