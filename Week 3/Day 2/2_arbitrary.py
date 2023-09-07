# arbitrary arguments (*)
def calculate_total(price, *args):
    for arg in args:
        total_cost = total_cost + arg

    return total_cost


cart1_total = calculate_total(4, 1, 23, 56, 4, 12, 3, 78, 90, 12)
cart2_total = calculate_total(34, 45, 12)

print(f"Total cost for cart 1 is ${cart1_total}")
print(f"Total cost for cart 2 is ${cart2_total}")


# arbitrary keyword arguments (**)

def save_user_info(**info):
    user_data = {
        **info
    }

    return user_data


my_info = save_user_info(
    name="tolu", email="tolu@mail.com", age=35, gender="male")

print(my_info)
