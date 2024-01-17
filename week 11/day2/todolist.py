# Making sure tasks inputed more than once
# only shows once in the list


# using set to avoid duplicates
tasks = set()

while True:
    user_tasks = input('What is your tasks? ').lower()

    if user_tasks == 'q':
        break
    else:
        tasks.add(user_tasks)

for idx, task in enumerate(tasks):
    print(f'{idx + 1} -> {task}')
