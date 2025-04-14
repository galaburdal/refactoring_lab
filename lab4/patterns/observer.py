class OrderObserver:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify_all(self, order):
        for observer in self._observers:
            observer.notify(order)
