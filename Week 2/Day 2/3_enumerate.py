# Define a list of items in the shopping cart
shopping_cart = [
    "milk",    # 1st iteration, item = milk
    "cereal",  # 2nd iteration, item = cereal
    "beans",   # 3rd iteration, item = beans
    "corn"     # 4th iteration, item = corn
]

# Print each item using index (not recommended)
print(f"Your no. 1 item is {shopping_cart[0]}")
print(f"Your no. 2 item is {shopping_cart[1]}")
print(f"Your no. 3 item is {shopping_cart[2]}")
print(f"Your no. 4 item is {shopping_cart[3]}")


# Print each item using a loop
for item in shopping_cart:
    print("Your no. 1 item is " + item)

# Print each item using enumerate to include item number
for num, item in enumerate(shopping_cart):
    print(f"Your no. {num + 1} item is {item}")
