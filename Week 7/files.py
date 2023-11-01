string = "Alice is \"smart\\\" and she is going to her mum's school"

# escape
string = '''
This is "line" 'one'

THis is line two'

ghkrp
'''

string = "Hello, how are you doing today?"

# print(string[0:9])

# print(string.lower())

# print("lo," in string.lower())

# Alice is "smart" and she is going to her mum's school

# Alice is "smart\" and she is going to her mum's school

age = 65

height = 60

string = "I am " + str(age) + " year old"

# string interpolation
# string = "I am John.\tI am tall.\nI am a fotballer"
string = "I am %s YEars old  AnD %s inches tall" % (age, height)

# string = "john23"

string_list = string.split()

print(string_list)

print('_'.join(string_list))
