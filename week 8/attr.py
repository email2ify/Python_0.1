class User:  
    # class attributes
    number_of_people = 0  # amount of people

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.registered()

    def login(self):
        print(f"{self.username} is successfully logged in")
    def create_post(self):
        print(f"{self.username} has successfully created a post")
    # class methods
    @classmethod
    def registered(cls):
        cls.number_of_people += 1

    @classmethod
    def say_hi(cls):
        print("Hi, world!")

    @staticmethod
    def add():
        return 2 + 1
    
    def __str__(self):
        return f"{self.username}'s information"
    
    def __repr__(self) -> str:
        pass


user1 = User("john", "john@mail.com")
user2 = User("Janice", "john@mail.com")

print(user1)
print(user2)