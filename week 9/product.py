# store - products
import csv

class Product:
    discount = 0.1
    all_products = []

    def __init__(self, name, price , quantity):
        assert price >= 0, f"Price of product ({name}) can't be less than zero"

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
    def get_products(cls):
        with open("products.csv", "r") as file:
            items = list(csv.DictReader(file))

            for item in items:
                product = Product(item["name"], float(item["price"]), int(item["quantity"]))

            return "products imported successfully"

    @classmethod
    def add_product():
        # add product
        pass

    @classmethod
    def all(cls):
        return cls.all_products

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"


product1 = Product("Crocs", 12, 10)

print(Product.get_products())

print(Product.all())


# print(Product.all())











# list1 = []
# set1 = set()

# append

# list1.append("john")
# list1.append("john")

# set1.add("james")
# set1.add("james")

# print(list1)
# print(set1)