class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация класса с атрибутами продукта"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity