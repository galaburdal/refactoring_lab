class Bike:
    def __init__(self, bike_type, frame, wheels, motor=None, price=0):
        self.bike_type = bike_type
        self.frame = frame
        self.wheels = wheels
        self.motor = motor
        self.price = price

    def __str__(self):
        return f"{self.bike_type} (Рама: {self.frame}, Колеса: {self.wheels}, Мотор: {self.motor if self.motor else 'Немає'}, Ціна: ${self.price})"

class BikeBuilder:
    def build_bike(self, bike_type):
        if bike_type == 'electric':
            return Bike('Електровелосипед', 'Алюмінієва', '28 дюймів', '500W', 800)
        else:
            return Bike('Звичайний велосипед', 'Сталева', '26 дюймів', None, 300)
