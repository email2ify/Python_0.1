fruits = ["apple", "orange", "banana", "cherry", "cheese"]


# append (add elemnt to end of a list)
fruits.append("mango")
# ouput: ["apple", "orange", "banana", "cherry", "cheese", "mango"]


# example 1 (print a list of names)
names = []
while True:
    name = input("Enter a name (or 'q' to quit): ")
    if name == "q":
        break
    names.append(name)

print(names)


# example 2 (return list of numbers greater than 20)
data = [12, 34, 22, 45, 15, 18, 9, 36, 27, 10]
selected_numbers = []  # numbers greater 20


for number in data:
    if number > 20:
        selected_numbers.append(number)

print(selected_numbers)
