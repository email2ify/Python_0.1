def add(x, y):
    return x + y


def add_1(x, y): print(x + y)


def add_2(x, y): return x + y


sum1 = add_1(1, 3)  # None
sum2 = add_2(1, 3)  # 4
print(sum2)

# sum1 = None
# sum2 = 4

total = add_2(3, 5)
print(total)


# lambda functions or anonymous functions
# lambda parameters : output(return value)

# so the add function can be written as:

# final_add = lambda x,y : x + y
new_sum = final_add(3, 8)
print(new_sum)


# use case of lambda functions
fruits = ['apple', 'orange', 'cherry']

cool = map(lambda x: x + " fruit", fruits)
print(list(cool))
