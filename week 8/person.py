class User:
    def __init__(self, username, age, email, password):
        self.username = username
        self.age = age
        self.email = email
        self.password = password

    def login(self):
        pass

    def logout(self):
        pass

    def create_post(self):
        pass
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 20:
            raise ValueError("Age must be between 20 and 30")
        self.__age = age

    def delete_post(self):
        pass


# dunder
class PremiumUser(User):
    def __init__(self, username, age, email, password, membership_card):
        super().__init__(username, age, email, password)
        self.membership_card = membership_card

    def edit_post(self):
        pass

    def watch_videos(self):
        pass

    def invite_friend(self):
        pass


prem_user = PremiumUser("john36", 29, "john@gmail.com", "password", "C$34-21")

