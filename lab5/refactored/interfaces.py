from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_invoice(self):
        pass

class PriceCalculable(ABC):
    @abstractmethod
    def calculate_total(self):
        pass
