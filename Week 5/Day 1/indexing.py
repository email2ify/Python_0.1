# indexing 

#          0        1       2       3        4        5
names = ["Alice", "Bob", "John", "James", "David", "Chris"]

# The first element of a list is at index 0
# and subsequent elements have increasing indices.

names[0]  # first element in the list
names[1]  # second element in the list
names[2]  # third element in the list
names[3]  # fourth element in the list
names[4]  # fifth element in the list
names[5]  # sixth element in the list

# Negative indexing
# Negative indices are used to access elements from the end of the list.

names[-1] # last element in the list
names[-2] # second to the last element in the list



# replacing elements using indexing
books = ["Book 1", "Book 2", "Book 3", "Book 4"]
books[0] = "The Storm"

# swapping elements using indexing
colors = ["red", "green", "blue"]
colors[0], colors[2] = colors[2], colors[0]
# "red"     "blue"      "blue"     "red"


# accessing nested elements using indexing
nested = [[1,2], [3,4], [5,6], [7,8]]

print(nested)
print(nested[2])

n_nested = [[3, [4, [8,9]]], 10]

[[3, [4, [8,9]]], 10]  # 0

[3, [4, [8,9]]]  # 1

[4, [8,9]]  # 1

[8,9] # 0


print(n_nested[0][1][1][0])