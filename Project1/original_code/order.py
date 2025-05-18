class Order:
    def __init__(self, client):
        self.client = client
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        if dish in self.dishes:
            self.dishes.remove(dish)

    def calculate_total(self):
        return sum(dish.price for dish in self.dishes)

    #refact
    a=4