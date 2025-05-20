from abc import ABC, abstractmethod

class Coffee(ABC):
    """Абстрактний клас кави"""

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class Espresso(Coffee):
    def get_description(self) -> str:
        return "Espresso"

    def get_cost(self) -> float:
        return 2.00


class Latte(Coffee):
    def get_description(self) -> str:
        return "Latte"

    def get_cost(self) -> float:
        return 3.50


class Americano(Coffee):
    def get_description(self) -> str:
        return "Americano"

    def get_cost(self) -> float:
        return 2.50


class Cappuccino(Coffee):
    def get_description(self) -> str:
        return "Cappuccino"

    def get_cost(self) -> float:
        return 3.00

