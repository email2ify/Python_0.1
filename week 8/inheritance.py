# superclass or parent class, base class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def roll(self):
        print(f"{self.name} is rolling over")

    def sleep(self):
        print(f"{self.name} is now sleeping")


# subclass or child class
class Cat(Animal):
    def speak(self):
        print('meow')

    def roll(self):
        print("I am dancing")


cat1 = Cat("Tin", 3)
cat1.sleep()

