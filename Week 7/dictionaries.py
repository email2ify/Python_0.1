# dictinaries

number = 78

cars = ['BMW', 'Mercedes', 'Mazda', 'Jeep']

thistuple = ("orange", "apple", "banana")

thisset = {"orange", "apple", "banana", "mango"}

# print(cars[0])

# dictionaries are:
# - ordered
# - values asscoiate with a key

# info = dict(name='john', email='john@example.com', height=60)

info = dict([('name', 'john'), ('email', 'john@example.com'), ('height', 60)])

# print(info)

car = {
    "brand": "Toyota",
    "model": "camry",
    "year": 2009,
    "expiry_date": 2014
}

print(car.items())

postions = {
    1: "john",
    2: "james",
    3: "bob",
    4: "charlie"
}

car = {
    "brand": "Toyota",
    "model": "camry",
    "year": 2009,
    "expiry_date": 2014
}

car["model"] = "highlander"
car.update({"brand": "ford"})
car["colors"] = ["red", "white"]
car.update({"plate_num": "EPE-A4123"})

car.pop("brand")

car.popitem()

car.clear()

print(car)





car.get("expiry_date", 2003)

print(car.values())

print('toyota' in car.values())

del car["model"]

print(car)


if "model" in car:
    print("A model exists for this car")
else:
    print("No model exists for this car")