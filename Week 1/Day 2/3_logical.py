# Logical operators
# and
# or
# not

# logical operators are used on conditional statements
# they are used to combine conditonal statements

veggies_finished = True
sunny_day = True
car1 = "BMW x1"
car2 = "BMW x1"
car3 = "Mercedes GLE SUV"

# The (and) operator returns True if both statements are True
if car1 == car2 and car2 == car3:
    print("This is a nice car, go for it")


# 90 - 100 = A
# 80 - 89 = B
# 70 - 79 = C
# 60 - 69 = D
grade = int(input("Grade? "))

# The (or) operator returns True if one of the statements is True
if grade > 80 or grade < 89:
    print("grade: B")


# The (not) operator reverses the result
# not True = False
# not False = True

sleepy = False
if not sleepy:
    print("let's stay awake and learn")
