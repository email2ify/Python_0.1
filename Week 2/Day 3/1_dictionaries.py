# Nested for loops
# Creating a list of student names
students = ["ben", "bob", "tom", "mary", "james"]

# Creating a list of states
states = ["New york", "los agenles", "oyo", "kaduna"]

# Looping through a range of values for 'i'
for i in range(1, 4):
    # Looping through a range of values for 'j'
    for j in range(1, 7):
        # Printing coordinates using 'i' and 'j'
        print(f"({i}, {j})")

# Creating a dictionary of student names and their corresponding states
students = {
    "ben": "New york",
    "bob": "los agenles",
    "tom": "oyo",
    "mary": "",
    "james": "kaduna",
}

# Looping through the student dictionary
for s in students:
    # Printing each student's name and their corresponding state
    print(f"{s} is from {students[s]}")

# Creating a list of dictionaries containing student information
students = [
    {"name": "Alice", "age": 18, "grade": "A", "city": "New York"},
    {"name": "Bob", "age": 17, "grade": "B", "city": "Los Angeles"},
    {"name": "Carol", "age": 19, "grade": "B+", "city": "Chicago"},
    {"name": "David", "age": 20, "grade": "A-", "city": "Houston"},
    {"name": "Eve", "age": 18, "grade": "A+", "city": "Miami"}
]

# Looping through the list of student dictionaries
for student in students:
    # Printing various information about each student
    print(f"{student['name']} is {student['age']} years old with grade {student['grade']} and is from {student['city']}")

# Looping through the list of student dictionaries
for student in students:
    # Looping through each key-value pair in the student dictionary
    for info in student:
        # Printing each piece of information
        print(f"{info}: {student[info]}\n")
