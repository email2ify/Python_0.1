# parameters
def greeting(name):
    print(f"Welcome {name}")


def greeting(name, age, gender):
    print(f"Welcome {name}, you are {age} years old and you're a {gender}")


greeting(gender="female", age=16, name='becky')


# default parameters


def greeting(name, age, gender="male"):
    print(f"Welcome {name}, you are {age} years old and you're a {gender}")


# positional argument
greeting("james", 27)

# keyword argument

# positional and keyword argument
greeting("john", gender="male", age=91)
