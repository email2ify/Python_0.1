import pprint
import random


list_ = [x for x in range(500) if x % 2 == 1]


new_list = []
for x in range(500):
    if x % 2 == 1:
        new_list.append(x)


# nested comprehensions

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# output: flattened = [1, 2, 3, 4, 5, 6, 7, 8, 9]

flattened = []
for sentence in matrix:
    for item in sentence:
        flattened.append(item)

flattened = [item for i in matrix for item in i]


sentences = ["This is a sentence.", "Python is fun.", "list comprehensions are nice."]

lengths = []
for sentence in sentences:
    lengths.append(len(sentence))


result = [
    i**2
    for i in range(1, 19)
    if i % 2 == 0 and i > 4
]

# "orange", "orange"
fruits = ["apple", "orange", "kiwi", "banana", "mango", "cherry", ]

newlist = [fruit for fruit in fruits if fruit != "banana"]


numbers = [1, 2, 3, 4, 5, 6, 7, 31, 8, 9]

even_or_odd = []
for num in numbers:
    if num % 2 == 0:
        even_or_odd.append("even")
    else:
        even_or_odd.append("odd")


even_or_odd = ["even" for num in numbers if num % 2 == 0]

a = ["even" if num % 2 == 0 else "odd" for num in numbers]

print(a)




users = [
    {"username": "bob", "email": "jt@gmail.com"},
    {"username": "charliechris", "email": "charliechris@gmail.com"},
    {"username": "john", "email": "john@gmail.com"}
]

email = "bob@gmail.com"
new_username = email.split('@')[0]  # jamesroudiger

all_usernames = [user["username"] for user in users]

while new_username in all_usernames:
    suffix = random.randint(1000, 9000)
    new_username += str(suffix)

users.append({"username": new_username, "email": email})

# print(all_usernames)


# pprint.pprint(users)