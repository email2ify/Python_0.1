def greeting(name, age, gender):
    print(f"Welcome {name}, you are {age} years old and you're a {gender}")


# positional argument
greeting("james", 27, "male")

# keyword argument
greeting(gender="female", age=16, name='becky')

# positional and keyword argument
greeting("john", gender="male", age=91)
