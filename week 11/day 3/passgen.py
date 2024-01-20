# Password Generator
# 1. Ask the user for the desired password length
# 2. Provide options: Uppercase, Lowercase, Numbers, Special Characters in their password.
# 3. Generate a password using the user's prefernces.
# 4. Display the password to the user.
# 5. Put everyting in a function.

# steps:

#1. User will input a desired password lenght
# 2. convert  desired password lenght to an integer
# 2/ using input, ask them if they want Uppercase, Lowercase...
# . # > do you want numbers [(y)es/(n)o]? y
    # > do you want upercase [(y)es/(n)o]? y
#  check their preferences and create a password using that.
  # e.g if a user want number, add number

import random
import string

password_length = int(input("How long do you want your password to be? "))

has_numbers = input("Do you want numbers in your password? (y/n) ") == 'y'
has_uppercase = input("Do you want uppercase letters in your password? (y/n) ") == 'y'
has_lowercase = input("Do you want lowercase letters in your password? (y/n) ")  == 'y'
has_special_chars = input("Do you want special characters in your password? (y/n) ")  == 'y'


password = ''

if has_numbers:
  password += string.digits

if has_uppercase:
  password += string.ascii_uppercase

if has_lowercase:
  password += string.ascii_lowercase

if has_special_chars:
  password += string.punctuation

# print(password)

final_password = ''

for i in range(password_length):
  final_password += random.choice(password)

print(final_password)

# print(''.join(random.choice(password) for i in range(password_length)))



# ASSIGNMENT
# how long is the password? 10

# how many numbers? 11
# how many uppercase
# how many lowercase
# how many special characters



a = ['dog', 'cat', 'camel', 'mouse']
# print(random.choice(a)) # selcts random item from a sequence
# print(random.randint(1, 67)) # selects random integer from a range
