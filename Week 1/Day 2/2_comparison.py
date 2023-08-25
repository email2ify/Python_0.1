# Comparison operators
# ==
# !=
# >
# <

car1 = "BMW x1"
car2 = "BMW x1"
car3 = "Mercedes GLE SUV"

# when comparing using comparison operators
# they evaluate expressions down to Boolean values
# returning either True or False

# prints True because car1 is the same as car2
print(car1 == car2)

# prints True because car1 is different from car3
print(car1 != car3)

# prints False because car1 is the same as car2
print(car1 != car2)


#  A peek into conditonals
# Using comparison operators with if statements

if car1 == car2:
    print("This is the same type of car")

if car1 != car2:
    print("This is not the same type of car")


fruit1 = input("What is the first fruit? ")
fruit2 = input("What is the second fruit? ")

if fruit1 == fruit2:
    print("This is the same type of fruit")

if fruit1 != fruit2:
    print("These are different fruits")


age = int(input("What is your age? "))

if age < 18:
    print("You cannot vote")
if age > 18:
    print("You can vote")
