# sets

thislist = ["orange", "apple", "banana", "orange"]

# sets are
# - unordered
# - no duplicates
# - True and 1, False and 0 are the same
thisset = {"orange", 23, 21.62, 1, 0, False, True}
newlist = list({"orange", 23, 21.62, 1, 0})


# add and update items to a set
thisset = {"orange", "apple", "banana", "mango"}

thislist = ["cherry", "guava", "starapple"]

thisset.add("kiwi")  # add item

# You can update a set with another set or a list
thisset.update(thislist)  # update set

# print(thisset)
# example output: {"orange", "apple", "banana", "mango", "kiwi", "cherry", "guava", "starapple"}


# remove items from a set
# returns error if item doesn't exist
# but error can be handled
try:
    thisset.remove("john")
except KeyError:
    print("item doesn't exist")

# does not retrun an error if item doesn't exist
thisset.discard("john")

# removes random items from a set
thisset.pop()

# empites a set (removes all items)
thisset.clear()

# print(thisset)
# output: set()

# delete thissset variable
# del thisset

# Join two or more sets
set1 = thisset.union(thislist)

print(set1)

print(thisset)


# An example (difference between updat() and union()):

# update
# folder1 (5)+3
# folder2 (3)

# folder1 (8)


# union
# folder1 (5)
#     +
# folder2 (3)

# folder3 (8)
