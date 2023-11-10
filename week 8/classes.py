# object oriented programming

class Car:
    def drive(self):
        print("barking")

    def park(self):
        print("roll over")

# A function within a class is a method

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def bark(self):
        print("bark")

    def roll(self):
        print("roll over")
    
    def sleep(self):
        print("sleep")
    
    def add_friend(self, friend: str):
        self.friends.append(friend)

d1 = Dog("james", 13)

d1.add_friend("jonathan")
d1.add_friend("david")

d2 = Dog("charlie", 16)
d2.add_friend("bob")


print(d1.friends)
print(d2.friends)