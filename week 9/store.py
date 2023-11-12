# store - products

class Product:
    discount = 0.1
    all_products = []

    def __init__(self, name, price , quantity):        
        assert price >= 0, "Price of product can't be less than zero"

        # assinging values
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all_products.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def get_discount(self):
        return self.price - (self.price * self.discount)

    @classmethod
    def all(cls):
        return cls.all_products

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"


product1 = Product("crocs", 30, 5)
product2 = Product("pan", 415, 3)

# print(product2.get_discount())

# print(product1.all())

# print(Product.all_products)

print(Product.all())
