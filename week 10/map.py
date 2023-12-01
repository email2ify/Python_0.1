# map and filter

# map(function, iterable)
# runs a function on an iterable
import pprint

numbers = [1, 2, 34, 56, 7]

def power(number):
    return number ** 3

new_numbers = []
for number in numbers:
    new_numbers.append(power(number))

new_numbers2 = [power(number) for number in numbers]  
# print(new_numbers2)

new_numbers = list(map(power, numbers))
# print(new_numbers)


strings = ["1", "2", "34", "56", "7"]


new_numbers = set(map(float, strings))


# dt
# integer (int)
# string (str)
# float
# boolean
# list, tu...


# print(new_numbers)



# convert each worker's ocupation to software engineer
workers = [
    {"name": "Sammy", "occupation": "Space Explorer", "personality": "Playful"},
    {"name": "Ashley", "occupation": "Botanical Scientist", "personality": "Curious"},
    {"name": "Jo", "occupation": "Musical Virtuoso", "personality": "Friendly"},
    {"name": "Jackie", "occupation": "Skydiving Instructor",
        "personality": "Adventurous"},
    {"name": "Charlie", "occupation": "Stand-up Comedian", "personality": "Humorous"},
    {"name": "Olly", "occupation": "Yoga Instructor", "personality": "Relaxed"}
]


# for worker in workers:
#     worker["old_occupation"] = worker["occupation"]
#     worker["occupation"] = "Software Engineer"


def change_occupation(worker):
    # add logic for age
    worker["occupation"] = "Fisherman"
    return worker

_ = list(map(change_occupation, workers))

pprint.pprint(workers)

# pprint.pprint(workers)

# boy = {"name": "Sammy", "age": 18}

# boy["age"] = 23

# boy["color"] = "dark"

# print(boy)
