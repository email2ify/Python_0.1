fruits = ["apple", "orange", "banana", "cherry", "cheese"]

# removing using index
removed_item = fruits.pop()
removed_item_2 = fruits.pop(1)

fruits.insert(0, removed_item)

print(fruits)
