# problem: TO-DO LIST

# allow a user to add tasks
# they should be able to quit the program (if they enter q)
# print the whole tasks they've added


# solution:

# 1. create an empty list to store the tasks (e.g tasks)

# 2. Enter a loop that allows the user to add tasks, until they decide to quit
    # a. ask them for the tasks
    # b. if the user enters "q" exit the loop
    # c. otherwise, add the task to the list(tasks)
    # print the whole tasks(list)

tasks = []

while True:
    user_tasks = input('What is your tasks? ').lower()
    if user_tasks == 'q':
        break
    else:
        tasks.append(user_tasks)
print(tasks)

#  assignment

# your to list:
# 1. write notes
# 2. go to the min mart
# 3. wash clothes
