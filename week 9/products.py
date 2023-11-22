# store - products
import csv


class Product:
    discount = 0.1
    all_products = []

    def __init__(self, name, price, quantity):
        assert price >= 0, f"Price of product ({name}) can't be less than zero"

        # assinging values
        self.name = name
        self.__price = price   # private attribute

        self.quantity = quantity
        self.all_products.append(self)

    @property  # (getters)
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value + 20
        return self.__price

    def calculate_total_price(self):
        return self.price * self.quantity

    def get_discount(self):
        return self.price - (self.price * self.discount)

    @classmethod
    def get_products(cls):
        with open("products.csv", "r") as file:
            items = list(csv.DictReader(file))

            for item in items:
                product = Product(item["name"], float(
                    item["price"]), int(item["quantity"]))

            return "products imported successfully"

    @classmethod
    def add_product(cls, *products):
        with open("products.csv", "a") as file:
            fields = ['name', 'price', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fields)

            for prd in products:
                writer.writerow({
                    'name': prd.name,
                    'price': prd.price,
                    'quantity': prd.quantity
                })
                print(f"{prd.name} has been added")

            return "All products have been added"

    def __connect_to_server(self):
        print("connected")

    def __secure_tls(self):
        print("secured")

    def __message_body(self):
        print(f"{self.name} has been added")

    def __send(self):
        print("email sent")

    def send_email(self):
        self.__connect_to_server()
        self.__secure_tls()
        self.__message_body()
        self.__send()

    @classmethod
    def all(cls):
        return cls.all_products

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"


class LuxuryProduct(Product):
    pass
