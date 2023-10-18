# count

fruits_1 = ["apple", "orange", "banana"]
fruits_2 = ["cherry", "cheese", "banana"]

all_fruits = fruits_1 + fruits_2


copy_fruits = all_fruits  # exact duplicate list
copy2_fruits = all_fruits.copy()  # initaial list
all_fruits = ['apple', 'orange', 'banana', 'cherry', 'cheese', 'banana']
for i in range(30):
    all_fruits.append('apple')

print(all_fruits.count('apple'))

print(all_fruits)


# sort

data = [12, 34, 22, 45, 15, 18, 9, 36, 27, 10]

data.sort()
all_fruits.sort()

# print(data)
# print(all_fruits)


# reverse

all_fruits.reverse()

# print(all_fruits)


# copy


# print(copy_fruits)
# print(copy2_fruits)

# clear

all_fruits.clear()

del all_fruits
print(all_fruits)