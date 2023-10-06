fruits_1 = ["apple", "orange", "banana"]
fruits_2 = ["cherry", "cheese", "banana"]

# You can concatenate several lists together using "+" sign
all_fruits = fruits_1 + fruits_2

print(fruits_1)
print(fruits_2)
print(all_fruits)


# extend (extend a list with another list)
fruits_1.extend(fruits_2)
# print(fruits_1)
# output: ['apple', 'orange', 'banana', 'cherry', 'cheese', 'banana']


# creating our own extend function
def our_extend(initial_list: list, extended_list: list):
    for item in extended_list:
        initial_list.append(item)
    
    return initial_list

first_list = ["apple", "orange", "banana"]
second_list = ["grape", "watermelon"]

our_extend(first_list, second_list)

