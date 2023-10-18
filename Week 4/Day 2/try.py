# Explanation of try, except, else, and finally blocks

# Example 1: How to use try, except, else, and finally blocks
try:
    pass  # Code that may raise exceptions
except NameError:  # <NameError> is just an example, it can be any error
    pass  # Handle division by zero
else:
    pass  # Code to execute if no exceptions occurred
finally:
    pass  # Cleanup code (will be executed no matter what)


# Example 2: Handling a ValueError exception
try:
    number = int(input("What's number 2? "))
    print(f"{number} is an integer")
except ValueError:
    print('not an integer')


# Example 3: Using else block to execute code when no exceptions occur
try:
    number_2 = int(input("What's number 2? "))
except ValueError:
    print('not an integer')
else:
    print(f"{number_2} is an integer")


# Example 4: Using finally block for cleanup code
try:
    x = int(input("What's x? "))
except ValueError:
    print('x is not an integer')
else:
    print(f"{x} is an integer")
finally:
    print('end of code')


# Example 5: Defining a function to get an integer input from the user
def get_int():
    while True:
        try:
            # Attempt to convert user input to an integer
            x = int(input("What's x? "))
        # This block runs if an exception (ValueError) is raised
        except ValueError:
            # Print an error message for invalid input
            print('x is not an integer')
        else:  # This block runs if input is successfully converted to an integer
            break  # Exit the loop since we have a valid integer
    return x  # Return the valid integer to the caller


# Example 6: A modified version of the get_int function
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print('x is not an integer')
        else:  # This block runs if input is successfully converted to an integer
            return x  # Return the valid integer to the caller immediately, exiting the function and the loop


# Example 7: Using the get_int function in the main function
def main():
    number = get_int()  # Call the get_int function to get an integer input
    print(f"{number} is x")


# Example 8: A simple function to determine food based on user input
# returning string based on conditions
def food():
    user_input = input('What food? ')

    if user_input == 'cheese':
        print('food is cheese')
        return 'cheese-food'
    elif user_input == 'rice':
        return 'rice-food'
    else:
        return 'unknown-food'
