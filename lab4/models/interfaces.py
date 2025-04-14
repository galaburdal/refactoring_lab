from abc import ABC, abstractmethod

class INotifier(ABC):
    @abstractmethod
    def notify(self, order):
        pass

class IOrderFactory(ABC):
    @abstractmethod
    def create_order(self, client):
        pass
