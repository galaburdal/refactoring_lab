from models.dish import Dish

class Menu:
    def __init__(self):
        self._dishes = []

    def add_dish(self, dish: Dish):
        '''Додає страву до меню'''
        if dish and isinstance(dish, Dish):
            self._dishes.append(dish)

    def get_dishes(self):
        '''Повертає список всіх страв'''
        return self._dishes
