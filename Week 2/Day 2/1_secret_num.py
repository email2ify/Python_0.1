# Set the number of attempts and the secret number
attempts = 6
secret_number = 8

# While loop: Keep looping as long as there are attempts left
while attempts > 0:
    # Get a number from the user
    user_num = int(input("What number? "))

    # Check if the user's number matches the secret number
    if user_num == secret_number:
        print("That's correct!")
        break  # Exit the loop when the guess is correct
    else:
        attempts -= 1  # Decrease attempts by 1
        print(f"Wrong! You have {attempts} attempts more")

# For loop: Iterate from 1 to 6
for i in range(1, 7):
    # Get a number from the user
    user_num = int(input("What number? "))

    # Check if the user's number matches the secret number
    if user_num == secret_number:
        print("That's correct!")
        break  # Exit the loop when the guess is correct
    else:
        attempts_left = 6 - i  # Calculate attempts left
        print(f"Wrong! You have {attempts_left} attempts more")
