# list comprehensions
# [expression for item in list]


# EXAMPLE 1

# return a new list with the items
# of orignal list multiplied by 2

orignal_list = [1, 2, 3, 4, 5, 6]

# 1st method using for loop & appending
new_list = []
for num in orignal_list:
    new_list.append(num * 2)

# 2nd method using list comprehension
new_list = [num * 2 for num in orignal_list]



# EXAMPLE 2

# return a new list with letters 
# in the names list lowered case

names = ["Sophia", "John", "SAMUEL", "bOb", "wiLLIAm"]

# 1st method using for loop & appending
new_names = []
for name in names:
    if name.startswith('S'):
        new_names.append(name.lower())

# 2nd method using list comprehension
new_names = [name.lower() for name in names]



# EXAMPLE 3

# return a new list with only even numbers
# using the numbers in data list

data = [12, 15, 34, 22, 45, 15, 18, 9, 36, 27, 10]

# 1st method using for loop & appending
even_nums = []
for number in data:
    if (number % 2) == 0:
        even_nums.append(number)

# 2nd method using list comprehension
even_nums = [num for num in data if num % 2 == 0]



# EXAMPLE 4

# return a new list with numbers
# only greater than 20 from data list 

data = [12, 34, 22, 45, 15, 18, 9, 36, 27, 10]

# 1st method using for loop & appending
selected_numbers = []
for number in data:
    if number > 20:
        selected_numbers.append(number)

# 2nd method using list comprehension
selected_numbers = [num for num in data if num > 20]
