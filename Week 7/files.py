from PIL import Image
# file = open('doc.txt')

# try:
#     pass
# finally:
#     file.close()

# reading from a file

# with open('doc.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)


# fruits = ['apple is color green', 'orange is color orange', 'cherry is color red']

# with open('doc.txt', 'w') as file:
#     # file.write('The footballer is a great one.\nThe man is a great one')
#     for fruit in fruits:
#         file.write(fruit + '\n')
#     file.writelines(fruits)

# with open('doc.txt', 'a') as file:
#     file.write('The school is big enough for all of us\n')


with open('doc.txt', 'r') as doc, open('new.txt', 'w+') as new:
    doc_lines = reversed(doc.readlines())
    for line in doc_lines:
        new.write((f"+ {line}"))
