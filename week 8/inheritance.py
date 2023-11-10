class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def roll(self):
        print(f"{self.name} is rolling over")

    def sleep(self):
        print(f"{self.name} is now sleeping")


class Cat(Animal):
    def __init__(self):
        pass

    def speak(self):
        print('meow')

    def roll(self):
        print("I am dancing")


cat1 = Cat()
cat1.roll()

