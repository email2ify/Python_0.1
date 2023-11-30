# constants 
import math

NUMBER = 3

# for _ in range(NUMBER):
#     print("🐕")


# unpacking
name = ["john", "ashley"]

first_name, last_name  = name 


first_name, _ = input('What is your name? ').split()

print(f"Welcome, {first_name}")


def convert_currency(dollar, nickel, cent):
    """
    Converts dollars and nickels to cent
    """
    cents = (100 * dollar) + (5 * nickel) + cent

    return f"{dollar} dollars, {nickel} nickels and {cent} cents is equals to {cents} cents"

money1 = (12, 65, 0)
c = convert_currency(*money1)
# convert_currency(12, 65, 0)
print(c)


money2 = {"nickel": 5,"cent": 1, "dollar": 13}
d = convert_currency(**money2)
# convert_currency(nickel=5, cent=1, dollar=13)

print(d)

def example(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

example(23, 45, 67, 89, age=65, school="primary")
