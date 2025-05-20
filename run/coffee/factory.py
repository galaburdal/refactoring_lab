from .base_coffee import Coffee, Espresso, Latte, Americano, Cappuccino


class CoffeeFactory:
    """Фабрика для створення кави"""

    # run/coffee/factory.py
    def create_coffee(self, coffee_type: str) -> Coffee:
        t = coffee_type.lower()
        if t == "espresso":
            return Espresso()
        elif t == "latte":
            return Latte()
        elif t == "americano":
            return Americano()
        elif t == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError(f"Unknown coffee type: {coffee_type}")
