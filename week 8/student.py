c = ["mango", "banana", "orange"]
d = ["cherry", "guava", "apple"]

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return f"<{self.name} {self.score}>"


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.registered_students = set()
    
    def add_student(self, student):
        if len(self.registered_students) < self.max_students:
            self.registered_students.add(student)
            return "Student successfully registered"
        return "Can't take any more students"
    
    def remove_student(self, student):
        self.registered_students.discard(student)

s1 = Student("john", 14, 65)
s2 = Student("james", 19, 95)
s3 = Student("bob", 23, 71)
s4 = Student("chris", 21, 82)

course1 = Course("anatomy", 3)

print(course1.add_student(s2))
print(course1.add_student(s1))
print(course1.add_student(s4))

print(course1.registered_students)

course1.remove_student(s2)
course1.remove_student(s1)
course1.remove_student(s3)

print(course1.registered_students)

