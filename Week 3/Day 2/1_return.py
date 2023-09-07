def my_function(foods: list):
    for food in foods:
        print(f"{food} is a fuit")


my_function(["apple", "banana", "cherry"])

# print vs return

# print


def add_numbers(a, b):
    result = a + b
    print(result)

# return


def add_numbers2(a, b):
    result = a + b
    return result


sum1 = add_numbers(3, 6)  # = None
sum2 = add_numbers2(3, 6)  # = 9

# This will cause an error because function called in sum1 does not return any value, it only prints it
print(sum1 + 5)
# This will work perfectly because function called in sum2 returns a value
print(sum2 + 5)

# pass
# The pass keyword can be used as a placeholder


def unknown():
    pass
