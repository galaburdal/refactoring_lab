class Order:
    def __init__(self, client):
        self._client = client
        self._dishes = []

    @property
    def client(self):
        return self._client

    def add_dish(self, dish):
        if dish not in self._dishes:
            self._dishes.append(dish)

    def remove_dish(self, dish):
        if dish in self._dishes:
            self._dishes.remove(dish)

    def calculate_total(self):
        return round(sum(dish.price for dish in self._dishes), 2)