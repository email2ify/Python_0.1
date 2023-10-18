months = [
    "January",  
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# slicing

# list[start : stop]


first_three_months = months[0:3]  # or months[:3]
print(first_three_months)
# Output: ['January', 'February', 'March']


spring_months = months[1:6]
print(spring_months)
# Output: ['February', 'March', 'April', 'May', 'June']


last_four_months = months[-4:]
print(last_four_months)
# Output: ['September', 'October', 'November', 'December']


all_months = months[:]
print(all_months)
