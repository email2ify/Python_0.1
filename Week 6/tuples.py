
# Lists are mutable
# You can change the items in a list

thislist = ["orange", "apple", "banana"]

thislist[0] = "cherry"

# print(thislist)
# output:  ["cherry", "apple", "banana"]


# Tuples are immutable
# You cannot change the items in a list

thistuple = ("orange", "apple", "banana")

# convert a list to a tuple
list_to_tuple = tuple(thislist)

# You can also create tuples without usign parantheses
singletuple = "john", "bob"

information = ("John", 31, True)

print(thistuple)
