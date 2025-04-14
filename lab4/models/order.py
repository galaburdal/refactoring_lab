class Order:
    def __init__(self, client):
        self.client = client
        self._dishes = []

    def add_dish(self, dish):
        '''Додає страву до замовлення'''
        self._dishes.append(dish)

    def get_total(self):
        '''Рахує суму за замовлення'''
        return sum(dish.price for dish in self._dishes)
