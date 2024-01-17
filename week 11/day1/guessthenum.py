# problem; guess the number
# have a secret number
# user input; the number they think it is
# tell them wrong or right


# solution

# 1. generate random number, then store as sceret number
# 2. ask the user to guess the number
# 3. convert useer's input to an integer
# 4. compare the user's guess w/ the secret number
    # a. if the guess is correct, print congratulatory message, end program
    # b. if the guess is incorrect, print a message and ask user to try again
            # i. if number of trials is less than user's trial
                #  try again
            # ii. if not, end program and reveal secret number
# 5. end the program

import random

num_of_trials = 5
secret = random.randint(90, 121)
print(secret)

while num_of_trials > 0:
    user_number = int(input('What is the secret number? '))
    if user_number == secret:
        print('You are correct')
        break
    else:
        print('wrong , try again')
        num_of_trials -=1

print(f'this is the secret nuber: {secret}')


#  don't print "try again" message when it is the last trial and the user still inputs the wrong number
# don't print the seceret number when the user is correct