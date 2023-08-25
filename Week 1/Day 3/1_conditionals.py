#  IF statemnts
x = input("What's x? ")
y = input("What's y? ")

if x > y:
    print("X is greater than y")

if x < y:
    print("x is less than y")

if x == y:
    print("x is equals to y")


# ELIF (else-if)
# The elif statement allows you to test multiple conditions in sequence after an initial if statement.
# If the condition following if is False, Python checks the conditions under elif one by one until a True condition is found.
# This prevents unnecessary checks once a True condition is encountered.
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
elif x == y:
    print("x is equals to y")

# ELSE
# The else statement follows an if or elif block and is executed when none of the preceding conditions are true.
# It provides a default action to take if no other conditions match
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equals to y")

# we could have done
if x != y:
    print("x is not equals to y")
elif x == y:
    print("x equals to y")

# a better approach would be:

if x != y:
    print("x is not equals to y")
else:
    print("x equals to y")
