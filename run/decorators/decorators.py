from run.coffee.base_coffee import Coffee

class CoffeeDecorator(Coffee):
    """Базовий клас-декоратор"""
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def get_description(self) -> str:
        return self._coffee.get_description()

    def get_cost(self) -> float:
        return self._coffee.get_cost()


class Milk(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Milk"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50


class Syrup(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Syrup"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.30


class WhippedCream(CoffeeDecorator):
    def get_description(self) -> str:
        return self._coffee.get_description() + ", Whipped Cream"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.70
