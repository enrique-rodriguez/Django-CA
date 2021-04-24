from .entity import Entity


class Product(Entity):
    def __init__(self, name, price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.price = price