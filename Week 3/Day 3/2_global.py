#  global variables

num_1 = 13
num_2 = 12


def addition():
    global num_1, num_2

    num_3 = 34  # local variable

    num_1 += 5

    num_2 += num_3

    print(num_3 + num_1)


addition()
