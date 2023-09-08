# docstrings

# Examples on how to use docstrings
def withdraw_money():
    """
    Withdraws a specified amount of money from the given account balance.
    """

    while True:
        # logic to handle withdrawal goes here
        pass


# More examples on to document your function
def greet(name):
    """
    This function greets a person.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width


def complex_function(param1, param2):
    """
    This is a more complex function.

    Parameters:
    param1 (int): The first parameter.
    param2 (str): The second parameter.

    Returns:
    bool: True if the operation succeeds, False otherwise.

    Raises:
    ValueError: If param2 is not in the correct format.
    """
    # Function code here
    pass


# Use help() to access documentation
help(calculate_area)


# Accessing the docstring
print(greet.__doc__)
