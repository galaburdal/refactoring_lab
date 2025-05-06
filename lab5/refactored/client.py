class Client:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Client: {self.name}, Address: {self.address}"
