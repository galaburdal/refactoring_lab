class Order:
    """Модель замовлення"""

    def __init__(self, description: str, cost: float):
        self.description = description
        self.cost = cost

    def __str__(self):
        return f"Order: {self.description} | Total: ${self.cost:.2f}"
