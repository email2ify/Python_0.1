car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1997,
    "expiry_date": 2014
}

# print(car["year"])


car_list = ["brand", "model", "year", "expiry_date"]

car.values()

# for x in car:
#     print(car[x])

c = [
    ('brand', 'Ford'),
    ('model', 'Mustang'),
    ('year', 1997),
    ('expiry_date', 2014)
]

# for key in car:
#     print(key)

# for key in car.key():
#     print(key)

# for value in car.values():
#     print(value)

# for key, value in car.items():
#     print(value)


# date = ('october', 1997)

# # unpacking
# month, year = date

# print(month)
# print(year)
# print(date)

car2 = car.copy()

car2['brand'] = "Mercedes"


# print('car1', car)
# print('car2', car2)


family = {
    "child1": {"name": "James", "dob": 2012},
    "child2": {"name": "John", "dob": 2005},
}

# print(family["child2"])

numbers = [23, 12, 13]

new_dict = {}

for number in numbers:
    new_dict[str(number)] = number ** 3
    
# print(new_dict)


newdict = {str(number): number**3 for number in numbers}

# print(newdict)

students = ["John", "James", "Bob", "Charles", "David"]

students_rank = {}

for student in students:
    s_idx = students.index(student)
    # students_rank[s_idx + 1] = student
    students_rank.update({(s_idx+1): student})


students_rank = {students.index(student)+1: student for student in students}

print(students_rank)
